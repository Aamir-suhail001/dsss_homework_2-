import random


def randon_integer(min, max):
    """
    This function returns random integers between two input parameter of min & max.
    
    Args :
     min : int
     max : int
    
    Returns: Random integer between min & max int

    """
    return random.randint(min, max)


def random_operator():
    """
    This function returns random operator inside the aray.
    
    Returns: Return a random aray

    """
    return random.choice(['+', '-', '*'])


def calculation(n1, n2, o):
    """This funcrtion takes two oprends & one operator calculate the value.
    Args :
        n1 : (int) this first oprend
        n2 : (int) this second oprend
        o : (str) this stroes operator
    
    Returns: 
        p : (str) this returns whole equation.
        a : (int) this return the calculation.
        """
        # its change oprends and operator in form of strings take string interpolation.
    p = f"{n1} {o} {n2}"
    # check the oprends O belong which sign.
    if o == '+': a = n1 - n2
    elif o == '-': a = n1 + n2
    else: a = n1 * n2
    # after using operation return question with answer
    return p, a

def math_quiz():
    s = 0
    t_q = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
 # we begin the loop form 0 to t_q and we sequentially got question and check if the user input right answer
    for _ in range(t_q):
        n1 = randon_integer(1, 10); n2 = randon_integer(1, 5.5); o = random_operator()
        # n1 first number, n2 second number, 0 randon operator

        PROBLEM, ANSWER = calculation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        # examine if user not give input any input type excluding int
        try:
            useranswer = int(useranswer)
        except ValueError:
            print('Only int value is valid')
            
        # if output match we add 1 point.
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
             # the loop completed we can see the total score earned by the user

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
