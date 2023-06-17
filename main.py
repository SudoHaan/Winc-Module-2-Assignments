# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Part 1
def greet(name, template='Hello, <name>!'):
    template = template.replace('<name>', name)
    return (f'{template}')

print(greet('Doc'))

#Part 2
def force(mass, body='earth'):
    bodies = {'mercury': 3.7,
              'venus': 8.9,
              'earth': 9.8,
              'moon': 1.6,
              'mars': 3.7,
              'jupiter': 23.1,
              'saturn': 9.0,
              'uranus': 8.7,
              'neptune': 11.0,
              'pluto': 0.7}
    gravity = bodies.get(body)
    force_n = gravity * mass

    #f = m * g

    
    return force_n

print(force(3,'uranus'))

# Part 3
def pull(m1, m2, d):
    # F = G * ((m1 * m2) / (d**2))
    pull = (6.674 * (10**-11))
    print(pull)
    pull_n = pull * ((m1 * m2) / (d**2))
    return pull_n

print(pull(800, 1500, 3))