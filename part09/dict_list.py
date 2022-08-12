# dict vs list
user1 = ['스펜서', 1.0, 0.9, 200, 60, 265, 260]
user2 = {
    'name' : '스펜서',
    'eye_L' : 1.0,
    'eye_R' : 0.9,
    'height' : 200,
    'weight' : 60,
    'foot_L' : 265,
    'foot_R' : 260,
}

user3 = {
    'name' : '스펜서',
    'eye' : { 'L' : 1.0, 'R' : 0.9},
    'height' : 200,
    'weight' : 60,
    'foot' : {'L' : 265, 'R' : 260},
}

user4 = {
    'name' : '스펜서',
    'eye' : [1.0, 0.9],
    'height' : 200,
    'weight' : 60,
    'foot' : [265, 260],
}
