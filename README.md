# iosxe
Python module to manage Cisco IOS XE devices via the rest API



## Device configuration
'''
!
transport-map type persistent webui HTTPS_WEBUI
!
username <username> privilege 15 secret 0 <password>
!
virtual-service csr_mgmt
 ip shared host-interface GigabitEthernet1
 activate
!
ip http secure-server
!
transport type persistent webui input HTTPS_WEBUI
!
'''