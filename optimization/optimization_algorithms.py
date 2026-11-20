

from optimization.optimization_problem import Optimization_Problem

import random


class Optimization_Algorithms():
    """
        Optimization class with different optimization method implementations
    """

    @classmethod
    def exhaustive_search(cls):
        """
            calculate the best values for toast and wait duration by searching all values exhaustively.
        """
        best_utility = float('-inf')
        best_solution = None

        for toast_duration in range(1,101):
            for wait_duration in range(1,101):
                utility = Optimization_Problem.utility(
                                toast_duration = toast_duration,
                                wait_duration = wait_duration)
                
                if utility > best_utility:
                    best_utility = utility
                    best_solution = (toast_duration,wait_duration)
        return best_solution, best_utility
    


    @classmethod
    def hill_climbing(cls):
        """
            calculate the best values for toast and wait duration by implementing Hill Climbing
        """
        # TODO: implement me 
        BestU = float('-inf')
        BestS_G = None
        BestU_G = float('-inf')

        r = 5
        while r > 0:
            r += -1
            ToastT = random.randint(1, 100)
            WaitT =  random.randint(1, 100)
            while True:
                improved = False

                for a in range(-1,2):
                    for b in range(-1,2):
                        WaitT_ = WaitT + b
                        ToastT_ = ToastT + a
                        if not (1 <= WaitT_ <= 100):
                            continue
                        if not (1 <= ToastT_ <= 100):
                            continue

                        utility = Optimization_Problem.utility(
                                            toast_duration = ToastT_,
                                            wait_duration = WaitT_)

                        
                        if utility > BestU:
                            BestU = utility
                            ToastT = ToastT_
                            WaitT = WaitT_
                            improved = True
                        if BestU > BestU_G:
                            BestS_G = (ToastT_,WaitT_)
                            BestU_G = BestU

                if not improved:
                    break

        return BestS_G, BestU_G



            

        return None, float('-inf')

    @classmethod
    def gradient_ascent(cls):
        """
            Calculate the best values for toast_duration, wait_duration and power.
            This will require a mixture of hill climbing and Gradient Ascent
        """
        # TODO: implement me
        BestU = float('-inf')
        BestS_G = None
        BestU_G = float('-inf')
        l_rate = 0.001    
        h = 0.0001
        r = 50
        while r > 0:
            r += -1
            ToastT = random.randint(1, 100)
            WaitT =  random.randint(1, 100)
            p_start = random.uniform(0,2)
            p_normal = p_start
            BestU = Optimization_Problem.utility(
    power = p_normal,
    toast_duration = ToastT,
    wait_duration = WaitT
)
            if BestU > BestU_G:
                BestU_G = BestU
                BestS_G = (ToastT, WaitT, p_normal)

            while True:
                improved = False

                for a in range(-1,2):
                    for b in range(-1,2):
                        WaitT_ = WaitT + b
                        ToastT_ = ToastT + a
                        if not (1 <= WaitT_ <= 100):
                            continue
                        if not (1 <= ToastT_ <= 100):
                            continue

                        p_minus = max(0.0, p_normal - h)
                        p_plus = min(2.0, p_normal + h)

                        utility_minus = Optimization_Problem.utility(power = p_minus,
                                                            toast_duration = ToastT_,
                                                            wait_duration = WaitT_)
                        utility_plus = Optimization_Problem.utility(power = p_plus,
                                                        toast_duration = ToastT_,
                                                        wait_duration = WaitT_)

                        gradient = (utility_plus - utility_minus) / (p_plus - p_minus)
                        p_new = p_normal + gradient*l_rate
                        p_new = max(0.0, min(2.0, p_new))


                        utility = Optimization_Problem.utility(power = p_new,
                                            toast_duration = ToastT_,
                                            wait_duration = WaitT_)
                        
                        if utility > BestU:
                            BestU = utility
                            ToastT = ToastT_
                            WaitT = WaitT_
                            p_normal = p_new
                            improved = True
                            if BestU > BestU_G:
                                BestS_G = (ToastT,WaitT,p_normal)
                                BestU_G = BestU

                if not improved:
                    break
            
            

                            

        return BestS_G, BestU_G



