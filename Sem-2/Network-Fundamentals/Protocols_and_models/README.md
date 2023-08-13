# Network Structure

3 Common elements for communication
* message source
* the channel
* messgage destination

Message (Source) -> Transmitter -> Transmission Medium -> Receiver-> Message Destinaition

(Data and infromations networks are capable of carrying many different types of communication )

## Communication Rules

* Encoding - Language
* Formatting - Salutation, recipent identity, closing phrase, sender identity
* Message size - Monologue or conversation ?
* Timing - Flow control / Timeout
* Delivery - Unicast, multicast or brodcast 

## Protocols

### Services 

* Addressing - Find out's the device
* Format - Structure of data
* Reliability and Flow control : Handling errors and controlling the rate of data delivery
* Sequencing - Confirms data is delivered in the correct order
* Application interface - mange communication with OS and installed software


### Functions of protocols 

HTTP -> TCP -> IP -> Ethernet 

* Governs the way that webserver and a web client interact, provides application interface
* Divides the HTTP message into smaller pieces, called segments, to be sent to web client. Provides reliability, flow control, sequencing
* Takes segments TCP, encapsulates them into packates, assign apporiate addresses and selects the best path to the destination host.
* Take the packets from the IP and format them to be transmitted over the network media. Provdies error detection.

### Protocol suites - Industry Standards 
* A set of protocols that work together to provide network communication service

### TCP / IP

* TCP/IP protocols are available for the application, transport and internet layer
* Access layer (LAN protocols) are Ethernet and WLAN (wireless LAN)

### Standard Organizations 
* Networking standards are developed BY International Standards Organization (ISO)
* The Internet Society (ISOC)
* The Internet Architecture Board (IAB)
* The Internet Engineering Task Force (IETF)
* The Internet of Electrical and Electronics Engineers (IEEE)
* The International Organization for Standardization (ISO)

### Internet Standards 
* Internet Corporation of Assigned Names and Numbers (ICANN)
    * Based in US 
    * Provides IP address allocation 
    * Management of Domain names 
    * Assignment of information used in TCP/IP protocol
* Internet Assigned Number Authority (IANA)
    * Responsible for overseeing and managing IP address allocation and protocols for ICANN
* Institute of Electrical & Electronic Engineers (IEEE)
    * One of the leading Standard producing organization in organizations of the world
    * IEEE 802 deals with LAN and MAN both wired and wireless
* International Organization for Standarization (ISO)
    * **ISO** term is meaning equal based on greek workd **isos**,
    * **ISO** is well know fro **OSI**
    * It is an objective to provide a protocol suite, (OSI protocol suite)

## TCP/IP and OSI Reference Models
* Assits in protocol design
* Fosters competition because products from different vendors can work together 
* Change in one layer is done other layers are unaffected
* Common language to describe networking functions and capabilites
* Reference models are used to better understand functions and process involved in the networking 

* Please - Do - Not - Throw - Selina - Pizza - Away
```
                            _________
                           /         /.
    .-------------.       /_________/ |
   /             / |      |         | |
  /+============+\ |      | |====|  | |
  ||C:\>whoami  || |      |         | |
  ||0xtheM7     || |      | |====|  | |
  ||            || |      |   ___   | |
  ||            || |      |  |166|  | |
  ||            ||/@@@    |   ---   | |
  \+============+/    @   |_________|./.
                     @          ..  ....'
  ..................@     __.'.'  ''
 /oooooooooooooooo//     ///
/................//     /_/
------------------

 Application    / \ |
 Presentation    |  |
 Session         |  |
 Transport       |  |
 Network         |  |
 Datalink        |  |
 Physical        | \ /
______________/ \ ______________
   |           |   
   |           |  Data 
   |           |  Network 
___|___________|________________
  \ /

                    / \
 Application        |   |
 Transport          |   |
 Internet           |   |
 Network Access     |   |
                    <-----   
    !\ ________________________/!\
    !!                         !! \
    !!                         !!  \
    !!                         !!  !
    !!                         !!  !
    !!                         !!  !
    !!                         !!  !
    !!                         !!  !
    !!                         !!  /
    !!_________________________!! /
    !/_________________________\!/
       __\_________________/__/!_
      !_______________________!/ )
    ________________________    (__
   /oooo  oooo  oooo  oooo /!   _  )_
  /ooooooooooooooooooooooo/ /  (_)_(_)
 /ooooooooooooooooooooooo/ /    (o o)
/C=_____________________/_/    ==\o/==
```
