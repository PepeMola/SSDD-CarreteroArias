#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import Ice
Ice.loadSlice('IceGauntlet.ice')

import IceGauntlet
import hashlib
import getpass
 
class Client(Ice.Application):
    def run(self, argv): 
        base = self.communicator().stringToProxy(argv[1])
        autenticacion = IceGauntlet.GestorMapasPrx.checkedCast(base)
    
        if not autenticacion:
            raise RuntimeError("Invalid proxy")

        autenticacion.publish(argv[2], "Hola")

        return 0

sys.exit(Client().main(sys.argv))

