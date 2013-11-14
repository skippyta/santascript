from random import choice, shuffle


# People playing Santa
CO_HANG = 'Hang'
CHU_PHUC = 'Phuc'
BAC_NHUNG = 'Nhung'
NATALIE = 'Natalie'  # Also getting a gift
ANNIE = 'Annie'
COLE = 'Cole'
ROB = 'Rob'
CO_BI = 'Bi'
CHU_LOC = 'Loc'
CO_CHRISTINA = 'Christina'
DAD = 'Thang'
MOM = 'Thao'
CO_LIEN = 'Lien'
CHU_LOI = 'Loi'
VECKY = 'Vecky'
SKIPPY = 'Skippy'
CO_VAN = 'Van'
DEANNA = 'Deanna'

SANTA_GROUPS = [
    [MOM, DAD],
    [CO_HANG, CHU_PHUC],
    [CO_BI, ROB],
    [COLE, ANNIE],
    [CHU_LOC, CO_CHRISTINA],
    [VECKY],
    [DEANNA, CO_VAN],
    [CO_LIEN,  CHU_LOI],
    [SKIPPY],
    [BAC_NHUNG, NATALIE]
]


# People getting gifts
COKI = 'Coki'
RACHEY = 'Rachel'
JOSHY = 'Josh'
OWEE = 'Owen'
PHIL = 'Philip'
BREIGHSTER = 'Breigh'
KATIE = 'Katie'
MATT = 'Matthew'
ASHLEY = 'Ashley'
# Natalie too


DRAW = [
    COKI,
    COKI,
    RACHEY,
    RACHEY,
    JOSHY,
    JOSHY,
    OWEE,
    OWEE,
    PHIL,
    PHIL,
    BREIGHSTER,
    BREIGHSTER,
    KATIE,
    KATIE,
    MATT,
    MATT,
    ASHLEY,
    ASHLEY,
    NATALIE,
    NATALIE
]


RELATIONS = {
    MOM: [COKI],
    CO_HANG: [PHIL, BREIGHSTER],
    CO_BI: [],
    COLE: [COKI],
    CHU_LOC: [RACHEY, JOSHY, OWEE],
    VECKY: [NATALIE],
    DEANNA: [],
    CO_LIEN: [KATIE, ASHLEY, MATT],
    SKIPPY: [COKI],
    BAC_NHUNG: [NATALIE]
}


FINAL = []
for santa in SANTA_GROUPS:
    paired = False
    relations = RELATIONS[santa[0]]
    while not paired:
        pick_one = choice(DRAW)
        DRAW.remove(pick_one)
        pick_two = choice(DRAW)
        if (pick_one == pick_two) or (pick_one in relations) or (pick_two in relations):
            DRAW.append(pick_one)
        else:
            FINAL.append((santa, [pick_one, pick_two]))
            DRAW.remove(pick_two)
            paired = True

print DRAW
for pairing in FINAL:
    santa, santees = pairing
    print '/'.join(santa), ':', ' and '.join(santees)
