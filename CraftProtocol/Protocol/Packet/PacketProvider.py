#!/usr/bin/env python

from CraftProtocol.Protocol.Packet.PacketDirection import PacketDirection
from CraftProtocol.Protocol.ProtocolState import ProtocolState


class PacketProvider(object):
    _PACKETS = {}

    @staticmethod
    def get_packet_class(protocol, state, direction, packet_id):
        return PacketProvider._PACKETS[protocol][state][direction][packet_id]

    @staticmethod
    def register(protocol, state, direction, packet_id, cls):
        protocol = int(protocol)
        state = int(state)
        direction = int(direction)
        packet_id = int(packet_id)

        if protocol not in PacketProvider._PACKETS:
            PacketProvider._PACKETS[protocol] = {
                ProtocolState.HANDSHAKING: {
                    PacketDirection.SERVERBOUND: {}, PacketDirection.CLIENTBOUND: {}
                },
                ProtocolState.STATUS: {
                    PacketDirection.SERVERBOUND: {}, PacketDirection.CLIENTBOUND: {}
                },
                ProtocolState.LOGIN: {
                    PacketDirection.SERVERBOUND: {}, PacketDirection.CLIENTBOUND: {}
                },
                ProtocolState.PLAY: {
                    PacketDirection.SERVERBOUND: {}, PacketDirection.CLIENTBOUND: {}
                }
            }

        if packet_id in PacketProvider._PACKETS[protocol][state][direction]:
            raise ValueError("This id is already registered")

        PacketProvider._PACKETS[protocol][state][direction][packet_id] = cls
