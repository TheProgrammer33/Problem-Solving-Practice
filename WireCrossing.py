

"""
An electrical routing channel has n wiring pins both at the top and the bottom of the channel and wires
are used to connect a pin at the top of the channel to a pin at the bottom of the channel. The 10-pin
routing channel and its wiring connections shown below can be specified as C = [8, 7, 4, 2, 5, 1, 9, 3, 10,
6]. The cardinality of C is 10 in this case, indicating the number of pins at the top and bottom. The wiring
connections are specified in that pin k at the top of the channel is connected with a straight-line wire to
pin C(k) at the bottom of the channel. In this example, pin 1 at the top is connected to pin 8 at the
bottom; pin 2 at the top is connected to pin 7 at the bottom; and so on. Notice that there are total 22
wire crossings in this example. [Picture]

Sample:
2
8 7 4 2 5 1 9 3 10 6
3 1 4 5 2

22
4
"""

def wireCrossing():
    numberOfChannels = int(input())
    channels = []
    for i in range(numberOfChannels):
        channels.append(input().split())
    
    for channel in channels:
        crossings = 0
        for pinOutput in channel:
            for otherPinOutput in channel[:channel.index(pinOutput)]:
                if (int(pinOutput) < int(otherPinOutput)):
                    crossings += 1
        print("There are " + str(crossings) + " wire crossings in routing channel " + str(channels.index(channel)+1))