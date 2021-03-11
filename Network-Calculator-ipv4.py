# https://www.youtube.com/watch?v=wI-tdeDPGlU&list=PLbIBj8vQhvm2OT4MpkrsKDDVuZ_RlNzli&index=1
# ipv4 - Calcultator

import re
class Ipv4NetCalc():
    def __init__(self, ip='', prefixo='', mascara='',
                rede='', broadcast='', numero_hosts=''):
        self.ip = ip
        self.prefixo = prefixo
        self.mascara = mascara
        self.rede = rede
        self.broadcast = broadcast
        self.numero_hosts = numero_hosts

        if self.ip == '':
            raise ValueError("IP Não enviado!")

        self.ip_tem_prefixo()

        if not self.is_ip():
            raise ValueError("IP Inválido")

        if not self.prefixo and not self.mascara:
            raise ValueError("Ou o prefixo ou a máscara devem ser enviados")

        print(self.ip, self.prefixo)
                
    def ip_tem_prefixo(self):
        #192.168.20.65/24
        ip_prefixo_regexp = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/{0-9}{1,2}$')

        if not ip_prefixo_regexp.search(self.ip):
            #print('Tem')
            return 
            #print('n tem')
        #return False

        divide_ip = self.ip.split('/')    
        self.ip = divide_ip[0]
        self.prefixo = divide_ip[1]
    
    def is_ip(self):
        ip_regexp = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$')
    
        if ip_regexp.search(self.ip):
            return True
        return False

if __name__ == '__main__':
    ipv4 = Ipv4NetCalc(ip='192.168.1.1/24')