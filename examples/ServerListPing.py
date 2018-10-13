#!/usr/bin/env python

import socket

import CraftProtocol


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("mc-pl.net", 25565))

    serializer = CraftProtocol.Protocol.Packet.PacketSerializer(
        CraftProtocol.Protocol.ProtocolVersion.MC_1_10,
        CraftProtocol.Protocol.Packet.PacketSerializer.Mode.CLIENT
    )

    serializer.write(sock, CraftProtocol.Protocol.v1_10.Packet.Handshaking.HandshakePacket(
        CraftProtocol.Protocol.ProtocolVersion.MC_1_10,
        "mc-pl.net",
        25565,
        CraftProtocol.Protocol.ProtocolState.STATUS
    ))

    serializer.state = CraftProtocol.Protocol.ProtocolState.STATUS

    serializer.write(sock, CraftProtocol.Protocol.v1_10.Packet.Status.RequestPacket())

    response = serializer.read(sock)

    if not isinstance(response, CraftProtocol.Protocol.v1_10.Packet.Status.ResponsePacket):
        print "Invalid packet received!"
        exit(1)

    print CraftProtocol.Chat.ChatSerializer.strip_colors(response.description["description"])


if __name__ == "__main__":
    main()
