def countingmeals(developers):
    m_count = {'standard': 0, 'vegetarian': 0, 'vegan': 0, 'diabetic': 0, 'gluten-intolerant': 0}

    for dev in developers:
        if 'meal' in dev:
            option = dev['meal']
            if option in m_count:
                m_count[option] += 1

    return m_count


list1 = [
    {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian'},
    {'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard'},
    {'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan'},
    {'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian'},
]

result = countingmeals(list1)

formatted_result = {key: value for key, value in result.items() if value > 0}
print(formatted_result)
