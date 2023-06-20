import exercise1
from time import time
import sys
import traceback

def test_exercise1():
    """Test if the code function of exercise 1 is correct"""
    try:
        # Test returned value
        start_time = time()
        res_100 = exercise1.fibonacci(100)
        duration_100 = time() - start_time
        assert res_100 == 927372692193078999176,\
            f"fibonacci(100) should equal 927372692193078999176, got {res_100}"

        # Test execution time
        start_time = time()
        exercise1.fibonacci(10000)
        duration_10000 = time() - start_time
        if duration_10000 < duration_100*110:
            print("Congratulation, your answer to exercise 1 works in linear "
                  "time. You recieve 3/3 points for this exercise")
        else:
            print("Congratulation, your answer to exercise 1 works. "
                  "Unfortunately, the execution time is not linear (execution "
                  f"time for with n=10000 was {duration_10000/duration_100}x "
                  "higher than time for n=100. You recieve only 1/3 points for "
                  "this exercise")
    except:
        ex, val, tb = sys.exc_info()
        traceback.print_exception(ex, val, tb)
        print("Sorry, your answer to exercise 1 crashes or do not provided "
              "expected result (see error above). You will recieve 0/3 points "
              " for this exercise")

if __name__ == "__main__":
    test_exercise1()
