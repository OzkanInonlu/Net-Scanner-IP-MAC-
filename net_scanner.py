import scapy.all as scapy
import optparse as opt
import subprocess as sb


def get_inputs():
    p_object = opt.OptionParser()
    p_object.add_option("-i","--ip", dest="ip_address")
    return p_object.parse_args()


def broadcasting(ip_address):
    # arp paketini olusturduk
    arp_request = scapy.ARP(pdst=ip_address)
    # scapy icinde hangi sinifin ne yaptigini gormek icin;
    # scapy.ls(scapy.ARP())

    # modem uzerinden yayin icin
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())

    combined_packet = broadcast / arp_request  # scapy dilinde bu iki paketi birlestir demek
    (answered, unanswered) = scapy.srp(combined_packet,
                                       timeout=1,verbose=True)  # timeout=1 --> cevap verilmezse bekleme yapmasin diye

    # answered.show()
    answered.summary()


(user_inputs, arg) = get_inputs()
ip_address=user_inputs.ip_address
broadcasting(ip_address)
