import pyshark
import queue

"""This file handles the streaming of packets into a shared queue"""


def RunPacketStream(interface: str, packet_queue: queue.Queue):
    capture = pyshark.LiveCapture(interface=interface)
    for packet in capture.sniff_continuously():
        packet_queue.put(packet)

