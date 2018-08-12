#!/usr/bin/env python

__all__ = [
    "Handshaking",
    "Status",
    "Login",
    "Play"
]

import CraftProtocol.Protocol.v1_10.Packet.Handshaking
import CraftProtocol.Protocol.v1_10.Packet.Login
import CraftProtocol.Protocol.v1_10.Packet.Play
import CraftProtocol.Protocol.v1_10.Packet.Status


def _register_packets():
    import types
    from CraftProtocol.Protocol.Packet.BasePacket import BasePacket
    from CraftProtocol.Protocol.Packet.PacketProvider import PacketProvider
    from CraftProtocol.Protocol.ProtocolState import ProtocolState
    from CraftProtocol.Protocol.ProtocolVersion import ProtocolVersion

    for name, cls in Handshaking.__dict__.items():
        if isinstance(cls, types.TypeType) and issubclass(cls, BasePacket):
            PacketProvider.register(ProtocolVersion.MC_1_10,
                                    ProtocolState.HANDSHAKING,
                                    cls.PACKET_DIRECTION,
                                    cls.PACKET_ID,
                                    cls)

    for name, cls in Status.__dict__.items():
        if isinstance(cls, types.TypeType) and issubclass(cls, BasePacket):
            PacketProvider.register(ProtocolVersion.MC_1_10,
                                    ProtocolState.STATUS,
                                    cls.PACKET_DIRECTION,
                                    cls.PACKET_ID,
                                    cls)

    for name, cls in Login.__dict__.items():
        if isinstance(cls, types.TypeType) and issubclass(cls, BasePacket):
            PacketProvider.register(ProtocolVersion.MC_1_10,
                                    ProtocolState.LOGIN,
                                    cls.PACKET_DIRECTION,
                                    cls.PACKET_ID,
                                    cls)

    for name, cls in Play.__dict__.items():
        if isinstance(cls, types.TypeType) and issubclass(cls, BasePacket):
            PacketProvider.register(ProtocolVersion.MC_1_10,
                                    ProtocolState.PLAY,
                                    cls.PACKET_DIRECTION,
                                    cls.PACKET_ID,
                                    cls)


_register_packets()
