DIGITS = [0,1,2,3,4,5,6,7,8,9]
THRESHOLD = 1e-5

for d1 in DIGITS:
    for d2 in DIGITS:
        for d3 in DIGITS:
            for d4 in DIGITS:
                if d1 == 0 and d3 == 0: continue
                numerator = int(f'{d1}{d2}')
                denominator = int(f'{d3}{d4}')
                if numerator >= denominator: continue
                if denominator == 0: continue
                value = numerator / denominator
                
                # XX/XX
                # trivial
                if d1 == d3 and d1 == d4 and d2 == d3 and d2 == d4: continue
                
                # AB/AB
                # trivial
                if d1 == d3 and d2 == d4 or d1 == d4 and d2 == d3: continue
                
                # AB/CD
                # ignore
                if d1 != d3 and d1 != d4 and d2 != d3 and d2 != d4: continue
                
                numerator_after_cancel = None
                denominator_after_cancel = None
                if d1 == d3 and d1 != 0:
                    numerator_after_cancel = d2
                    denominator_after_cancel = d4
                elif d1 == d4 and d1 != 0:
                    numerator_after_cancel = d2
                    denominator_after_cancel = d3
                elif d2 == d3 and d2 != 0:
                    numerator_after_cancel = d1
                    denominator_after_cancel = d4
                elif d2 == d4 and d2 != 0:
                    numerator_after_cancel = d1
                    denominator_after_cancel = d3
                
                if numerator_after_cancel == None and denominator_after_cancel == None: continue
                if denominator_after_cancel == 0: continue
                value_after_cancel = numerator_after_cancel / denominator_after_cancel
                if abs(value - value_after_cancel) < THRESHOLD: print(f'{d1}{d2}/{d3}{d4}')
