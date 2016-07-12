# iosxe
Python module to manage Cisco IOS XE devices via the rest API

### IOS-XE API Introduction
[http://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/restapi/restapi/RESTAPIintro.html]
(http://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/restapi/restapi/RESTAPIintro.html)


### IOS-XE API Reference
[http://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/restapi/restapi.html]
(http://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/restapi/restapi.html)


### Device configuration
```
http://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/configuration/csr1000Vswcfg/RESTAPI.html#96914
!
transport-map type persistent webui HTTPS_WEBUI
!
username <username> privilege 15 secret 0 <password>
!
interface GigabitEthernet1
 ip address <ip_address> <subnet_mask>
!
virtual-service csr_mgmt
 ip shared host-interface GigabitEthernet1
 activate
!
ip http secure-server
!
transport type persistent webui input HTTPS_WEBUI
!
```