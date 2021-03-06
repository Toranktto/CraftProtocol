:mod:`CraftProtocol` --- Minecraft network protocol and NBT in Python 2.7.
==========================================================================

.. module:: CraftProtocol
   :synopsis: Minecraft network protocol and NBT in Python 2.7.

**Source code:** `CraftProtocol <https://github.com/Toranktto/CraftProtocol/tree/master/CraftProtocol>`_

--------------

This module provide high level interface for handling Named Binary Tags (NBT) and Minecraft network packets.

.. warning::
    This documentation is not complete.

Named Binary Tags (NBT)
-----------------------

Creating in-memory NBT tags:

.. code-block:: python

    from CraftProtocol import NBT

    tag = NBT.NBTTagCompound()
    tag["example_int_list_key"] = NBT.NBTTagList(NBT.NBTTagByte)
    tag["example_int_list_key"].append(NBT.NBTTagByte(0x00))
    tag["example_int_list_key"].append(NBT.NBTTagByte(0x0F))
    tag["example_string_key"] = NBT.NBTTagString("string")
    tag["example_double_key"] = NBT.NBTTagDouble(120.1351)

.. warning::
    You can't assign a native python value to NBTTagCompound key.
    Use class that inherits from NBTBase.

    +---------------------------+---------------------------+
    | Python Type               | NBT Type                  |
    +===========================+===========================+
    | NoneType                  | NBTBase                   |
    +---------------------------+---------------------------+
    | str                       | NBTTagString              |
    +---------------------------+---------------------------+
    | unicode                   | NBTTagString              |
    +---------------------------+---------------------------+
    | int                       | NBTTagInt                 |
    +---------------------------+---------------------------+
    | int                       | NBTTagShort               |
    +---------------------------+---------------------------+
    | int                       | NBTTagByte                |
    +---------------------------+---------------------------+
    | long                      | NBTTagLong                |
    +---------------------------+---------------------------+
    | float                     | NBTTagFloat               |
    +---------------------------+---------------------------+
    | float                     | NBTTagDouble              |
    +---------------------------+---------------------------+
    | dict                      | NBTTagCompound            |
    +---------------------------+---------------------------+
    | list                      | NBTTagList                |
    +---------------------------+---------------------------+
    | list                      | NBTTagByteArray           |
    +---------------------------+---------------------------+
    | list                      | NBTTagIntArray            |
    +---------------------------+---------------------------+
    | list                      | NBTTagLongArray           |
    +---------------------------+---------------------------+

    Remember that NBT Types with "Array" suffix can store only one NBT Type which is prefixed
    and NBTTagList can store only one choosed by user (in constructor) NBT Type.

To serialize NBT tag to stream (file-like or socket object):

.. code-block:: python

    from CraftProtocol.NBT import NBTSerializer

    NBTSerializer.write(stream, tag)

or deserialize from stream:

.. code-block:: python

    from CraftProtocol.NBT import NBTSerializer

    tag = NBTSerializer.read(stream)

.. note::
    NBTSerializer does not support compression. If you want to handle compressed NBT tags, use
    appropriate module for this, for example ``gzip``.

To convert NBT Value to Python Value:

.. code-block:: python

    nbt_string = tag["example_string_key"]
    native_string = nbt_string.get()

Packets
-------

Documentation of Minecraft network protocol can be found at http://wiki.vg.
Currently implemented versions of this protocol:

    - 1.8.x
    - 1.10.x
    - 1.12.2

.. note::
    In described examples, we use 1.10.x protocol.

Creating packet:

.. code-block:: python

    from CraftProtocol.Protocol import ProtocolVersion
    from CraftProtocol.Protocol import ProtocolState
    from CraftProtocol.Protocol.v1_10 import Packet

    packet = Packet.Handshaking.HandshakePacket(ProtocolVersion.MC_1_10, "hostname", 25565, ProtocolState.STATUS)

To know arguments for packet constructor, see http://wiki.vg.

If you want to serialize packets, use:

.. code-block:: python

    from CraftProtocol.Protocol import ProtocolVersion
    from CraftProtocol.Protocol import Packet

    serializer = CraftProtocol.Protocol.Packet.PacketSerializer(
        CraftProtocol.Protocol.ProtocolVersion.MC_1_10,
        CraftProtocol.Protocol.Packet.PacketSerializer.Mode.CLIENT
    )
    serializer.write(stream, packet)

To deserialize packets from stream (e.g. from socket object):

.. code-block:: python

    from CraftProtocol.Protocol import ProtocolVersion
    from CraftProtocol.Protocol import Packet

    serializer = CraftProtocol.Protocol.Packet.PacketSerializer(
        CraftProtocol.Protocol.ProtocolVersion.MC_1_10,
        CraftProtocol.Protocol.Packet.PacketSerializer.Mode.CLIENT
    )
    packet = serializer.read(stream)

.. warning::
    Different protocols may have different packets. See http://wiki.vg for details.

.. warning::
    Some packets is not implemented in CraftProtocol (only in ``Play`` protocol state).
    If you want to know list of implemented packets, see source code.

.. warning::
    You must manually change serializer protocol state if necessary. Default state is ``Handshaking``.
    For example, in ``Server List Ping`` after sending Handshake packet state must be switched to ``Status``.

.. note::
    Valid packet must inherits from ``CraftProtocol.Protocol.Packet.BasePacket`` class.

Chat
----

If you want to strip colors from chat (``dict``) object (e.g. from ``ChatMessageClientPacket`` packet) use:

.. code-block:: python

    from CraftProtocol.Chat import ChatSerializer

    raw_text = ChatSerializer.strip_colors(chat)

To serialize chat in legacy format use:

.. code-block:: python

    from CraftProtocol.Chat import ChatSerializer

    chat = ChatSerializer.translate_legacy(raw_text)


.. note::
    Serializing chat in modern (JSON) format is not currently supported.

Chat Objects
------------

.. class:: CraftProtocol.Chat.ChatMode

    .. note::
        This class is used to enum purposes only. You don't have to create new instances.

    .. attribute:: ENABLED

        This is default mode.

    .. attribute:: HIDDEN

        In this mode, chat is hidden.

    .. attribute:: COMMANDS

        In this mode, only commands can be send to server.

.. class:: CraftProtocol.Chat.ChatSerializer

    .. note::
        This class is static. You don't have to create new instances.

    .. staticmethod:: strip_colors(chat)

        Strip colors in chat (``dict``) message and return it.

        :param chat: chat message in modern JSON format
        :type chat: dict

    .. staticmethod:: translate_legacy(text, code="&")

        Translate colored chat message (like this ``&aHello &bWorld``) to paragraph-prefixed legacy format.

        :param text: text to translate
        :param code: character that is replaced to paragraph
        :rtype: unicode

Inventory Objects
-----------------

.. class:: CraftProtocol.Inventory.Inventory(window_id, title, inventory_type, slots_number, entity_id=None)

    :param window_id: inventory window id
    :param title: inventory title in chat format
    :param inventory_type: inventory type
    :param slots_number: number of items in inventory
    :param entity_id: only used if inventory type is ``EntityHorse``.
    :type window_id: int
    :type title: dict
    :type inventory_type: basestring enum
    :type slots_number: int
    :type entity_id: int

    .. note::
        Currently there is no class that has inventory type enum defined.

    .. method:: get_window_id()

        Return inventory window id.

        :rtype: int

    .. method:: get_title()

        Return inventory title.

        :rtype: dict

        .. note::
            Inventory title uses Chat format.

    .. method:: get_type()

        Return inventory type.

        :rtype: unicode enum

        .. note::
            Currently there is no class that has this enum defined.

    .. method:: get_slots()

        Return items in this inventory.

        :rtype: list (CraftProtocol.Inventory.SlotData)

    .. method:: get_entity_id()

        Return inventory entity id.

        :rtype: int or None

        .. note::
            Used only when Inventory Type is ``EntityHorse``.

    .. method:: __getitem__(index)

        Return item at specified index.

        :param index: index
        :type index: int
        :rtype: CraftProtocol.Inventory.SlotData

    .. method:: __setitem__(index, value)

        Set item at specified index.

        :param index: index
        :param value: slot data
        :type index: int
        :type value: CraftProtocol.Inventory.SlotData

    .. method:: __delitem__(index)

        Set item at specified index to empty slot.

        :param index: index
        :type index: int

    .. method:: __len__()

        Return number of items in this inventory.

        :rtype: int

    .. method:: __iter__()

        The same as __iter__() of get_slots().

        :rtype: iter

    .. method:: copy()

        Return copy of this inventory.

        :rtype: CraftProtocol.Inventory.Inventory

.. class:: CraftProtocol.Inventory.SlotData(item_id, count=0, damage=0, tag=None)

    :param item_id: item id
    :param count: item count
    :param damage: item variant
    :param tag: item NBT tag
    :type item_id: int
    :type count: int
    :type damage: int
    :type tag: CraftProtocol.NBT.NBTTagCompound or None

    .. staticmethod:: empty()

        Return empty slot.

        :rtype: CraftProtocol.Inventory.SlotData

    .. method:: get_id()

        Return slot item id.

        :rtype: int

    .. method:: get_count()

        Return number of items in this slot.

        :rtype: int

    .. method:: set_count(count)

        Set number of items in this slot.

        :param count: items count
        :type count: int

    .. method:: get_damage()

        Return slot item variant.

        :rtype: int

    .. method:: set_damage(damage)

        Set slot item variant.

        :param damage: item variant
        :type damage: int

    .. method:: get_tag()

        Return NBT tag of this slot.

        :rtype: CraftProtocol.NBT.NBTTagCompound or None

    .. method:: set_tag(tag)

        Set NBT tag of this slot.

        :param tag: NBT tag
        :type tag: CraftProtocol.NBT.NBTTagCompound or None

    .. method:: has_tag()

        Return ``True`` if slot has NBT tag.

        :rtype: bool

World Objects
-------------

.. class:: CraftProtocol.World.World(world_type, dimension, difficulty)

    :param world_type: world type
    :param dimension: world dimension
    :param difficulty: world difficulty
    :type world_type: CraftProtocol.World.WorldType basestring enum
    :type dimension: CraftProtocol.World.WorldDimension int enum
    :type difficulty: CraftProtocol.World.WorldDifficulty int enum

    .. method:: get_world_type()

        Return world type.

        :rtype: CraftProtocol.World.WorldType unicode enum

    .. method:: get_dimension()

        Return world dimension.

        :rtype: CraftProtocol.World.WorldDimension int enum

    .. method:: get_difficulty()

        Return world difficulty.

        :rtype: CraftProtocol.World.WorldDifficulty int enum

.. class:: CraftProtocol.World.Location(x, y, z, yaw=0.00, pitch=0.00)

    :param x: x
    :param y: y
    :param z: z
    :param yaw: yaw
    :param pitch: pitch
    :type x: float
    :type y: float
    :type z: float
    :type yaw: float
    :type pitch: float

    .. method:: get_x()

        Return x.

        :rtype: float

    .. method:: set_x(x)

        Set x.

        :param x: new x
        :type x: float

    .. method:: get_y()

        Return y.

        :rtype: float

    .. method:: set_y(y)

        Set y.

        :param y: new y
        :type y: float

    .. method:: get_z()

        Return z.

        :rtype: float

    .. method:: set_z(z)

        Set z.

        :param z: new z
        :type z: float

    .. method:: get_yaw()

        Return yaw.

        :rtype: float

    .. method:: set_yaw(yaw)

        Set yaw.

        :param yaw: new yaw
        :type yaw: float

    .. method:: get_pitch()

        Return pitch.

        :rtype: float

    .. method:: set_pitch(pitch)

        Set pitch.

        :param pitch: new pitch
        :type z: float



.. class:: CraftProtocol.World.WorldDimension

    .. note::
        This class is used to enum purposes only. You don't have to create new instances.

    .. attribute:: NETHER

        Represent Nether dimension.

    .. attribute:: OVERWORLD

        Represent natural dimension.

    .. attribute:: END

        Represent The End dimension.

.. class:: CraftProtocol.World.WorldDifficulty

    .. note::
        This class is used to enum purposes only. You don't have to create new instances.

    .. attribute:: PEACEFUL

        Represent easiest difficulty.

    .. attribute:: EASY

        Represent easy difficulty.

    .. attribute:: NORMAL

        Represent normal difficulty.

    .. attribute:: HARD

        Represent hard difficulty.

.. class:: CraftProtocol.World.WorldType

    .. note::
        This class is used to enum purposes only. You don't have to create new instances.

    .. attribute:: DEFAULT

        Represent default map type.

    .. attribute:: FLAT

        Represent super flat map type.

    .. attribute:: LARGE_BIOMES

        Represent map type with large biomes.

    .. attribute:: AMPLIFIED

        Represent amplified map type.

    .. attribute:: DEFAULT_1_1

        Represent legacy map type.

Protocol Objects
----------------

.. class:: CraftProtocol.Protocol.ProtocolState

    .. note::
        This class is used to enum purposes only. You don't have to create new instances.

    .. attribute:: HANDSHAKING

        Represent ``Handshaking`` protocol state.

    .. attribute:: STATUS

        Represent ``Status`` (``Server List Ping``) protocol state.

    .. attribute:: LOGIN

        Represent ``Login`` protocol state.

    .. attribute:: PLAY

        Represent ``Play`` protocol state.

.. class:: CraftProtocol.Protocol.ProtocolVersion

    .. note::
        This class is used to enum purposes only. You don't have to create new instances.

    .. attribute:: MC_1_8

        Represent protocol version that is used by Minecraft 1.8.x.

    .. attribute:: MC_1_10

        Represent protocol version that is used by Minecraft 1.10.x.

    .. attribute:: MC_1_12_2

        Represent protocol version that is used by Minecraft 1.12.2.
