from main import calculate_average_age


def test_calculate_average_age_without_family_size():
    lines = [
        '0,1,Pclass,3,4,5,Age,SibSp',
        '1,0,1,0,0,0,10,2',
        '2,0,1,0,0,0,20,3',
        '3,0,2,0,0,0,30,4',
        '4,0,2,0,0,0,40,5',
        '5,0,3,0,0,0,50,6',
        '6,0,3,0,0,0,60,7',
    ]
    assert calculate_average_age(lines) == (15.0, 35.0, 55.0)


def test_calculate_average_age_with_family_size_2():
    lines = [
        '0,1,Pclass,3,4,5,Age,SibSp',
        '1,0,1,0,0,0,10,2',
        '2,0,1,0,0,0,20,3',
        '3,0,2,0,0,0,30,4',
        '4,0,2,0,0,0,40,5',
        '5,0,3,0,0,0,50,6',
        '6,0,3,0,0,0,60,7',
    ]
    assert calculate_average_age(lines, consider_family_size=True, family_size=2) == (10.0, 0, 0)


def test_calculate_average_age_with_family_size_4():
    lines = [
        '0,1,Pclass,3,4,5,Age,SibSp',
        '1,0,1,0,0,0,10,2',
        '2,0,1,0,0,0,20,3',
        '3,0,2,0,0,0,30,4',
        '4,0,2,0,0,0,40,5',
        '5,0,3,0,0,0,50,6',
        '6,0,3,0,0,0,60,7',
    ]
    assert calculate_average_age(lines, consider_family_size=True, family_size=4) == (0, 30.0, 0)


def test_calculate_average_age_with_family_size_7():
    lines = [
        '0,1,Pclass,3,4,5,Age,SibSp',
        '1,0,1,0,0,0,10,2',
        '2,0,1,0,0,0,20,3',
        '3,0,2,0,0,0,30,4',
        '4,0,2,0,0,0,40,5',
        '5,0,3,0,0,0,50,6',
        '6,0,3,0,0,0,60,7',
    ]
    assert calculate_average_age(lines, consider_family_size=True, family_size=7) == (0, 0, 60.0)


def test_calculate_average_age_with_invalid_data():
    lines = [
        '0,1,Pclass,3,4,5,Age,SibSp',
        '1,0,1,0,0,0,10,2',
        '2,0,1,0,0,0,,3',
        '3,0,2,0,0,0,Тридцать,4',
        '4,0,2,0,0,0,40,5',
        '5,0,3,0,0,0,50,6',
        '6,0,3,0,0,0,60,7',
    ]
    assert calculate_average_age(lines) == (10.0, 40.0, 55.0)
