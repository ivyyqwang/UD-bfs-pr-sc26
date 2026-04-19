//
// Created by alefel on 12/07/23.
//

#ifndef UPDOWN_MMESSAGE_H
#define UPDOWN_MMESSAGE_H

#include <iostream>
#include <iomanip>
#include <assert.h>
#include <memory>
#include <cstring>
#include "lanetypes.hh"


// the number of words in the payload at maximum
#define MAX_PAYLOAD     9

namespace basim {

    enum class MType{
        M1Type = 0,
        M2Type = 1,
        M3Type = 2,
        M3Type_M = 3,
        M4Type = 4,
        M4Type_M = 5,
    };

    class MMessage {
    private:
        // used to trace the source of the message
        eventword_t srcEventWord;

        // Destination event word/Destination event label
        // The destination event word contains information about the event to be triggered into execution at the destination.
        eventword_t eventWord;

        // Continuation word / continuation event label
        // The continuation word to be triggered following the destination event's execution.
        eventword_t continuationWord;
        
        // Custom user data. Note: Make sure you do not double use.
        // It is not part of the message in the architecture.
        // Currently used for
        //  * carrying the MPI tag across to different MPI ranks
        uint64_t userData;

        // PayLoad len
        uint64_t len;

        // Payload data 
        //std::shared_ptr<word_t []> payload;
        word_t* payload;

        // Type of Message
        MType mtype;

        // Mode of messages
        uint8_t mode;

        // Destination Address
        Addr dstAddr;

        uint8_t isGlobal; // 0:local address, 1: global address, -1: others

    public:
        MMessage() = delete;

        MMessage(MMessage const &) = delete;

        //MMessage &operator=(MMessage const &) = delete;

        MMessage(eventword_t xc, eventword_t xe, MType _mtype) {
            setXc(xc);
            setXe(xe);
            mtype = _mtype;
            payload = nullptr;
            len = 0;
            dstAddr = 0;
            srcEventWord = -1;
            isGlobal = 0; // Default is local memory
        }

        ~MMessage(){
            if(payload != nullptr)
                delete[] payload;
        }

        void setIsGlobal(uint8_t _isGlobal) { isGlobal = _isGlobal; }

        uint8_t getIsGlobal() { return isGlobal; }

        void setXe(eventword_t newXe) { eventWord = newXe; }
        
        void setXc(eventword_t newXc) { continuationWord = newXc; }

        eventword_t getXe() { return eventWord; }

        eventword_t getXc() { return continuationWord; }

        uint64_t getUserData() {return userData;}
        void setUserData(uint64_t data) {userData = data;}

        MType getType(){return mtype;}

        void setType(MType _type) { mtype = _type; }

        void addpayload(word_t* data){
            for(int i = 0; i < len; i++)
                payload[i] = data[i];
        }
        
        word_t* getpayload(){return payload;}
        
        bool isStore(){return ((mode & 0x1) == 1);}
        
        void setMode(int _mode){mode = _mode;}

        uint8_t getMode() {return mode;}
        
        void setLen(uint64_t _len){
            BASIM_ERROR_IF(_len > MAX_PAYLOAD, "Payload can have 9 elements at maximum.");

            len = _len;
            if (payload != nullptr)
                delete[] payload;
            if(_len > 0)
                payload = new word_t[len];
            else
                payload = nullptr;
        }
        
        uint64_t getLen(){return len;}

        uint64_t getMsgSize() {
            /* FIXME: should the message type also be part of the message? */
            return (len + 1 /* Dst Event Word / Dst Addr*/ + 1 /* Continuation Word*/) * sizeof(word_t);
        }
        
        Addr getdestaddr() { return dstAddr; }
        
        void setdestaddr(Addr _destaddr) {dstAddr = _destaddr; }

        eventword_t getSrcEventWord() { return srcEventWord; }

        void setSrcEventWord(eventword_t _srcEventWord) { srcEventWord = _srcEventWord; }

        // NEEDS TO BE DIVISABLE BY 8! (for MPI_Alltoallv)
        static const size_t getMsgMaxSize() {
             // srcEventWord             eventWord          continuationWord;
            return sizeof(eventword_t) + sizeof(eventword_t) + sizeof(eventword_t) +
                // userData            len               payload                    mtype
                sizeof(uint64_t) + sizeof(uint64_t) + MAX_PAYLOAD * sizeof(word_t) + sizeof(MType) + 
                // mode              dstAddr        isGlobal      padding to make the message aligned to 128 Bytes
                sizeof(uint8_t) + sizeof(Addr) + sizeof(uint8_t) + 2;
        }

        // serialize method to convert class into a byte buffer
        std::vector<char> serialize() const {
            std::vector<char> buffer(MMessage::getMsgMaxSize());
            char* ptr = buffer.data();
            
            // Xe
            std::memcpy(ptr, &eventWord, sizeof(eventword_t));
            ptr += sizeof(eventword_t);

            // Xc
            std::memcpy(ptr, &continuationWord, sizeof(eventword_t));
            ptr += sizeof(eventword_t);

            std::memcpy(ptr, &mtype, sizeof(MType));
            ptr += sizeof(MType);

            std::memcpy(ptr, &srcEventWord, sizeof(eventword_t));
            ptr += sizeof(eventword_t);

            std::memcpy(ptr, &userData, sizeof(uint64_t));
            ptr += sizeof(uint64_t);

            std::memcpy(ptr, &len, sizeof(uint64_t));
            ptr += sizeof(uint64_t);

            std::memcpy(ptr, &mode, sizeof(uint8_t));
            ptr += sizeof(uint8_t);

            std::memcpy(ptr, &dstAddr, sizeof(Addr));
            ptr += sizeof(Addr);

            std::memcpy(ptr, &isGlobal, sizeof(uint8_t));
            ptr += sizeof(uint8_t);
            
            if(len != 0) {
                std::memcpy(ptr, payload, len*sizeof(word_t));
            }

            return buffer;
        }

        static std::unique_ptr<MMessage> deserialize(char* ptr) {

            eventword_t xe, xc;
            MType mtype;

            std::memcpy(&xe, ptr, sizeof(eventword_t));
            ptr += sizeof(eventword_t);

            std::memcpy(&xc, ptr, sizeof(eventword_t));
            ptr += sizeof(eventword_t);

            std::memcpy(&mtype, ptr, sizeof(MType));
            ptr += sizeof(MType);

            // create the class
            auto m = std::make_unique<MMessage>(xc, xe, mtype);

            eventword_t srcEventWord;
            std::memcpy(&srcEventWord, ptr, sizeof(eventword_t));
            ptr += sizeof(eventword_t);
            m->setSrcEventWord(srcEventWord);

            uint64_t tmpValue64;
            std::memcpy(&tmpValue64, ptr, sizeof(uint64_t));
            ptr += sizeof(uint64_t);
            m->setUserData(tmpValue64);

            std::memcpy(&tmpValue64, ptr, sizeof(uint64_t));
            ptr += sizeof(uint64_t);
            m->setLen(tmpValue64); // also creates a pointer for payload
        
            uint8_t tmpValue8;
            std::memcpy(&tmpValue8, ptr, sizeof(uint8_t));
            ptr += sizeof(uint8_t);
            m->setMode(tmpValue8);

            Addr tmpAddr;
            std::memcpy(&tmpAddr, ptr, sizeof(Addr));
            ptr += sizeof(Addr);
            m->setdestaddr(tmpAddr);

            std::memcpy(&tmpValue8, ptr, sizeof(uint8_t));
            ptr += sizeof(uint8_t);
            m->setIsGlobal(tmpValue8);

            if(m->getLen() != 0) {
                char* payloadPtr = reinterpret_cast<char*>(m->getpayload());
                std::memcpy(payloadPtr, ptr, m->getLen()*sizeof(word_t));
            }

            return m;
        }

        /**
         * @brief Serialize into a preallocated buffer
         */
        void serializeInto(char *buffer) {
            char *ptr = buffer;
            // Xe
            std::memcpy(ptr, &eventWord, sizeof(eventword_t));
            ptr += sizeof(eventword_t);

            // Xc
            std::memcpy(ptr, &continuationWord, sizeof(eventword_t));
            ptr += sizeof(eventword_t);

            std::memcpy(ptr, &mtype, sizeof(MType));
            ptr += sizeof(MType);

            std::memcpy(ptr, &srcEventWord, sizeof(eventword_t));
            ptr += sizeof(eventword_t);

            std::memcpy(ptr, &userData, sizeof(uint64_t));
            ptr += sizeof(uint64_t);

            std::memcpy(ptr, &len, sizeof(uint64_t));
            ptr += sizeof(uint64_t);

            std::memcpy(ptr, &mode, sizeof(uint8_t));
            ptr += sizeof(uint8_t);

            std::memcpy(ptr, &dstAddr, sizeof(Addr));
            ptr += sizeof(Addr);

            std::memcpy(ptr, &isGlobal, sizeof(uint8_t));
            ptr += sizeof(uint8_t);
            
            if(len != 0) {
                std::memcpy(ptr, payload, len*sizeof(word_t));
            }
        }


        void printMessage() {
            std::vector<char> buffer = this->serialize();
            for(size_t i=0; i<buffer.size(); ++i) {
                printf("%02x ", buffer[i] & 0xff);
                if((i + 1) % 16 == 0) {
                  printf("\n");
                }
            }
            if(buffer.size() % 16 != 0) {
                printf("\n");
            }
            fflush(stdout);
        }
    };

typedef MMessage* MMessagePtr;


inline std::ostream &operator<<(std::ostream &str, MMessage &m) {
    int type = static_cast<int>(m.getType());
    int isGlobal = static_cast<int>(m.getIsGlobal());
    int mode = static_cast<int>(m.getMode());
    str << "m: xe: " << m.getXe().eventword << ", xc: " << m.getXc().eventword << ", srcEvent: " <<
            m.getSrcEventWord().eventword << ", userData: " << m.getUserData() << ", length: " << 
            m.getLen() << ", mode: " << mode << ", type: " << type << 
            ", dstAddr: 0x" << std::hex << m.getdestaddr() << std::dec << ", global: " << isGlobal;
    str << std::hex << ", payload: [";
    for (size_t i = 0; i < m.getLen(); ++i) {
        if(i > 0) str << ", ";
        str << "0x" << m.getpayload()[i];
    }
    str << "]" << std::dec;
    return str;
}


    // Need to rewrite this.
    //inline std::ostream &operator<<(std::ostream &str, M1Message &mMessage) {
    //    str << "m: 0x" << std::hex << mMessage.getM() << ", len: 0x" << mMessage.getLen() << ", xptr: 0x"
    //        << mMessage.getXptr() << "Xc: 0x" << mMessage.getXc() << ", Xe: 0x" << mMessage.getXe();
    //    str << "(0x0" << std::setw(8) << std::setfill('0')
    //        << (mMessage.getM() << 26 || mMessage.getLen() << 22 || mMessage.getXptr() << 17 ||
    //            mMessage.getXc() << 12 || mMessage.getXe());
    //    str << ") " << std::dec;
    //    return str;
    //}

    //inline std::ostream &operator<<(std::ostream &str, M2Message &mMessage) {
    //    str << "destaddr: 0x" << std::hex << mMessage.getdestaddr() << "m: 0x" << mMessage.getM() << ", len: 0x"
    //        << mMessage.getLen() << ", xptr: 0x"
    //        << mMessage.getXptr() << "Xc: 0x" << mMessage.getXc() << ", Xe: 0x" << mMessage.getXe();
    //    str << "(0x0" << std::setw(8) << std::setfill('0')
    //        << (mMessage.getdestaddr() << 27 || mMessage.getM() << 25 || mMessage.getLen() << 22 ||
    //            mMessage.getXptr() << 17 ||
    //            mMessage.getXc() << 12 || mMessage.getXe()
    //                    << 7);
    //    str << ") " << std::dec;
    //    return str;
    //}

    //inline std::ostream &operator<<(std::ostream &str, M3Message &mMessage) {
    //    str << "destaddr: 0x" << std::hex << mMessage.getdestaddr() << "m: 0x" << mMessage.getM() << ", x2: 0x"
    //        << mMessage.getX2() << ", x1: 0x"
    //        << mMessage.getX1() << "Xc: 0x" << mMessage.getXc() << ", Xe: 0x" << mMessage.getXe();
    //    str << "(0x0" << std::setw(8) << std::setfill('0')
    //        << (mMessage.getdestaddr() << 27 || mMessage.getM() << 26 || mMessage.getX2() << 22 ||
    //            mMessage.getX1() << 17 ||
    //            mMessage.getXc() << 12 || mMessage.getXe()
    //                    << 7);
    //    str << ") " << std::dec;
    //    return str;
    //}

    //inline std::ostream &operator<<(std::ostream &str, M4Message &mMessage) {
    //    str << std::hex << "destaddr: 0x" << mMessage.getdestaddr() << "m: 0x" << mMessage.getM() << ", numops: 0x"
    //        << mMessage.getNumops() << ", xop: 0x"
    //        << mMessage.getXop() << "Xc: 0x" << mMessage.getXc() << ", Xe: 0x" << mMessage.getXe();
    //    str << "(0x0" << std::setw(8) << std::setfill('0')
    //        << (mMessage.getdestaddr() << 27 || mMessage.getM() << 26 || mMessage.getNumops() << 22 ||
    //            mMessage.getXop() << 17 ||
    //            mMessage.getXc() << 12 || mMessage.getXe()
    //                    << 7);
    //    str << ") " << std::dec;
    //    return str;
    //}
}

#endif //UPDOWN_MMESSAGE_H
