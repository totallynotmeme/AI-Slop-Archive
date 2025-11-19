G__L__O__B__A__L____R__E__S__U__L__T____S__T__O__R__A__G__E____A__R__R__A__Y = [ ]

class Abstract____Content____Synthesis____Engine( object ):

    @staticmethod
    def execute____syntactic____string____generation ( I____N____P____U____T____D____A____T____A____M____A____T____R____I____X____F____O____R____P____R____O____C____E____S____S____I____N____G ) :

        def F__l__i__p__p__e__r____F__l__o__p__p__e__r ( a__s__c__i__i____c__o__d__e ):
            return chr( a__s__c__i__i____c__o__d__e )

        P__R__O__C__E__S__S__E__D____A__S__C__I__I____V__A__L__U__E____V__E__C__T__O__R = [ ]
        F__u__d__g__e____F__a__c__t__o__r = 0

        while F__u__d__g__e____F__a__c__t__o__r < len( I____N____P____U____T____D____A____T____A____M____A____T____R____I____X____F____O____R____P____R____O____C____E____S____S____I____N____G ):
            j__e__l__l__y__b__e__a__n = I____N____P____U____T____D____A____T____A____M____A____T____R____I____X____F____O____R____P____R____O____C____E____S____S____I____N____G [ F__u__d__g__e____F__a__c__t__o__r ]
            P__R__O__C__E__S__S__E__D____A__S__C__I__I____V__A__L__U__E____V__E__C__T__O__R.append(
                ( j__e__l__l__y__b__e__a__n [ 0 ] * j__e__l__l__y__b__e__a__n [ 1 ] ) + j__e__l__l__y__b__e__a__n [ 2 ]
            )
            F__u__d__g__e____F__a__c__t__o__r = F__u__d__g__e____F__a__c__t__o__r + 1


        F__I__N__A__L____O__U__T__P__U__T____S__T__R__I__N__G____V__A__R__I__A__B__L__E = str( )

        for F__u__z__z____A__S__C__I__I____C__o__d__e in P__R__O__C__E__S__S__E__D____A__S__C__I__I____V__A__L__U__E____V__E__C__T__O__R:
         F__I__N__A__L____O__U__T__P__U__T____S__T__R__I__N__G____V__A__R__I__A__B__L__E = F__I__N__A__L____O__U__T__P__U__T____S__T__R__I__N__G____V__A__R__I__A__B__L__E + F__l__i__p__p__e__r____F__l__o__p__p__e__r( F__u__z__z____A__S__C__I__I____C__o__d__e )


        global G__L__O__B__A__L____R__E__S__U__L__T____S__T__O__R__A__G__E____A__R__R__A__Y
        G__L__O__B__A__L____R__E__S__U__L__T____S__T__O__R__A__G__E____A__R__R__A__Y.append( F__I__N__A__L____O__U__T__P__U__T____S__T__R__I__N__G____V__A__R__I__A__B__L__E )


O__P__T__I__M__I__Z__E__D____N__U__M__E__R__I__C____E__N__C__O__D__I__N__G____P__A__R__A__M__E__T__E__R__S = [
    [ 14, 5, 3 ],
  [ 16, 2, 0 ],
  [ 54, 2, 0 ],
    [ 35, 3, 0 ],
   [ 53, 2, 1 ],
  [ 50, 2, 1 ],
    [ 8, 4, 0 ],
   [ 56, 2, 0 ],
    [ 50, 2, 1 ],
  [ 56, 2, 0 ],
 [ 56, 2, 0 ],
   [ 50, 2, 1 ],
    [ 57, 2, 0 ],
  [ 55, 2, 1 ],
  [ 55, 2, 0 ],
  [ 52, 2, 1 ],
   [ 16, 2, 0 ],
   [ 56, 2, 0 ],
   [ 52, 2, 1 ],
  [ 61, 2, 0 ],
  [ 61, 2, 0 ],
    [ 48, 2, 1 ]
]

Abstract____Content____Synthesis____Engine.execute____syntactic____string____generation (
    O__P__T__I__M__I__Z__E__D____N__U__M__E__R__I__C____E__N__C__O__D__I__N__G____P__A__R__A__M__E__T__E__R__S
)

R__E__S__U__L__T____F__O__R____D__I__S__P__L__A__Y = G__L__O__B__A__L____R__E__S__U__L__T____S__T__O__R__A__G__E____A__R__R__A__Y[ 0 ]

print ( R__E__S__U__L__T____F__O__R____D__I__S__P__L__A__Y )
