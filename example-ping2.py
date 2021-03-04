# https://www.youtube.com/watch?v=UROnGOeAQOg
import subprocess

def ping_ip(ip):
    (output, error) = subprocess.Popen(('ping', ip, '-c', '2')), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    if b'bytes from' in output:
        return "HOST UP"
    elif b'Destination Host Unreachable' is output:
        return "HOST DOWN"
    elif error:
        return "DNS ERROR"
    else:
        return "UNKNOWN"

# l = ''  ## opcional
with open('arquivo') as f:
    for ip in f:
        ip = ip.strip('\n')
        response = ping_ip(ip)
        result = ('%s,%s \n' % (ip, response))
#       l = l+result ## opcional
# file = open('output.txt', 'w')
# file.write(l)
# file.close()
