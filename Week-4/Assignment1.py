'''
Write a Python function histogram(l) that takes as input a list of integers with repetitions and returns a list of pairs as follows:.

for each number n that appears in l, there should be exactly one pair (n,r) in the list returned by the function, where r is the number of repetitions of n in l.

the final list should be sorted in ascending order by r, the number of repetitions. For numbers that occur with the same number of repetitions, arrange the pairs in ascending order of the value of the number.

For instance:

>>> histogram([13,12,11,13,14,13,7,7,13,14,12])
[(11, 1), (7, 2), (12, 2), (14, 2), (13, 4)]

>>> histogram([7,12,11,13,7,11,13,14,12])
[(14, 1), (7, 2), (11, 2), (12, 2), (13, 2)]

>>> histogram([13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7])
[(11, 2), (12, 2), (7, 4), (13, 4), (14, 4)]
'''
from MergeSort import MergeSort, Merge
def histogram(A):
	A = MergeSort(A, 0, len(A)) # Returns a sorted list
	yellow = green = 0
	C = []
	counter = 0
	while green < len(A):
		if A[green] == A[yellow]:
			green += 1
			counter += 1
		else:
			C.append((A[yellow], counter))
			yellow = green
			counter = 0
	if counter > 0:
		C.append((A[yellow], counter))
	C = sortOutput(C)
	return C

def sortOutput(A):
	for (f, n) in A:
		A.sort(key=lambda x:x[1])
	return A

# Testing
actualOutput = histogram([310 ,310 ,310 ,310 ,310 ,970 ,970 ,970 ,970 ,970 ,770 ,770 ,906 ,906 ,906 ,906 ,906 ,906 ,906 ,906 ,906 ,199 ,199 ,199 ,199 ,199 ,199 ,199 ,866 ,866 ,866 ,866 ,866 ,866 ,866 ,866 ,866 ,866 ,314 ,314 ,314 ,314 ,314 ,314 ,966 ,966 ,966 ,966 ,695 ,695 ,695 ,695 ,695 ,695 ,695 ,695 ,695 ,695 ,359 ,359 ,359 ,961 ,961 ,961 ,961 ,961 ,961 ,961 ,801 ,801 ,839 ,839 ,839 ,839 ,574 ,574 ,322 ,322 ,322 ,322 ,322 ,322 ,322 ,322 ,322 ,322 ,506 ,506 ,506 ,602 ,602 ,602 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,614 ,870 ,870 ,870 ,870 ,870 ,870 ,870 ,870 ,381 ,381 ,381 ,381 ,533 ,533 ,675 ,675 ,675 ,480 ,480 ,480 ,480 ,480 ,480 ,480 ,772 ,772 ,772 ,772 ,772 ,772 ,772 ,772 ,772 ,218 ,218 ,218 ,218 ,218 ,218 ,218 ,218 ,197 ,197 ,197 ,197 ,197 ,141 ,141 ,141 ,141 ,141 ,123 ,123 ,123 ,123 ,123 ,689 ,689 ,689 ,689 ,689 ,689 ,689 ,689 ,689 ,606 ,606 ,606 ,606 ,606 ,606 ,606 ,41 ,41 ,41 ,41 ,41 ,41 ,41 ,41 ,41 ,839 ,839 ,811 ,811 ,811 ,811 ,811 ,811 ,705 ,705 ,705 ,705 ,705 ,705 ,705 ,705 ,705 ,705 ,584 ,584 ,584 ,584 ,584 ,584 ,584 ,584 ,579 ,579 ,579 ,579 ,579 ,579 ,90 ,90 ,90 ,90 ,90 ,90 ,99 ,99 ,99 ,99 ,99 ,99 ,99 ,99 ,491 ,491 ,491 ,491 ,491 ,491 ,491 ,642 ,642 ,642 ,642 ,642 ,642 ,642 ,486 ,486 ,486 ,486 ,486 ,486 ,852 ,852 ,852 ,852 ,852 ,852 ,852 ,852 ,300 ,300 ,300 ,300 ,300 ,300 ,300 ,619 ,619 ,619 ,619 ,619 ,619 ,619 ,554 ,554 ,554 ,429 ,429 ,429 ,429 ,689 ,689 ,689 ,689 ,689 ,689 ,689 ,320 ,320 ,592 ,592 ,592 ,592 ,196 ,196 ,196 ,196 ,196 ,811 ,811 ,811 ,811 ,811 ,436 ,436 ,436 ,436 ,436 ,520 ,520 ,520 ,520 ,520 ,520 ,520 ,865 ,865 ,865 ,147 ,147 ,147 ,147 ,147 ,147 ,147 ,147 ,147 ,147 ,73 ,73 ,73 ,76 ,76 ,76 ,406 ,406 ,406 ,406 ,406 ,406 ,406 ,406 ,406 ,313 ,313 ,313 ,313 ,313 ,847 ,847 ,847 ,847 ,847 ,847 ,198 ,198 ,198 ,198 ,198 ,930 ,930 ,536 ,536 ,536 ,316 ,316 ,316 ,416 ,416 ,416 ,416 ,416 ,416 ,416 ,416 ,416 ,765 ,765 ,765 ,765 ,765 ,765 ,765 ,765 ,468 ,468 ,468 ,468 ,468 ,468 ,468 ,468 ,468 ,833 ,833 ,833 ,833 ,833 ,833 ,833 ,833 ,58 ,58 ,58 ,58 ,58 ,58 ,36 ,36 ,36 ,36 ,36 ,36 ,36 ,36 ,36 ,36 ,498 ,498 ,498 ,498 ,144 ,144 ,144 ,144 ,483 ,483 ,483 ,483 ,830 ,830 ,830 ,830 ,830 ,830 ,701 ,701 ,701 ,701 ,701 ,701 ,701 ,701 ,701 ,655 ,655 ,490 ,490 ,490 ,490 ,490 ,490 ,490 ,490 ,135 ,135 ,429 ,429 ,429 ,429 ,429 ,429 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,8 ,901 ,901 ,219 ,219 ,219 ,219 ,219 ,219 ,219 ,219 ,668 ,668 ,668 ,668 ,668 ,668 ,668 ,968 ,968 ,477 ,477 ,477 ,277 ,277 ,277 ,277 ,277 ,277 ,277 ,277 ,277 ,277 ,])
expectedOutput = [(135, 2), (320, 2), (533, 2), (574, 2), (655, 2), (770, 2), (801, 2), (901, 2), (930, 2), (968, 2), (73, 3), (76, 3), (316, 3), (359, 3), (477, 3), (506, 3), (536, 3), (554, 3), (602, 3), (675, 3), (865, 3), (144, 4), (381, 4), (483, 4), (498, 4), (592, 4), (966, 4), (123, 5), (141, 5), (196, 5), (197, 5), (198, 5), (310, 5), (313, 5), (436, 5), (970, 5), (58, 6), (90, 6), (314, 6), (486, 6), (579, 6), (830, 6), (839, 6), (847, 6), (199, 7), (300, 7), (480, 7), (491, 7), (520, 7), (606, 7), (619, 7), (642, 7), (668, 7), (961, 7), (99, 8), (218, 8), (219, 8), (490, 8), (584, 8), (614, 8), (765, 8), (833, 8), (852, 8), (870, 8), (41, 9), (406, 9), (416, 9), (468, 9), (701, 9), (772, 9), (906, 9), (8, 10), (36, 10), (147, 10), (277, 10), (322, 10), (429, 10), (695, 10), (705, 10), (866, 10), (811, 11), (689, 16)]
print(actualOutput == expectedOutput)

actualOutput = histogram([936 ,936 ,936 ,936 ,936 ,936 ,936 ,936 ,131 ,131 ,131 ,131 ,83 ,83 ,83 ,83 ,83 ,83 ,83 ,486 ,486 ,486 ,486 ,486 ,486 ,75 ,75 ,75 ,75 ,75 ,594 ,594 ,594 ,594 ,594 ,594 ,594 ,215 ,215 ,215 ,215 ,215 ,215 ,215 ,215 ,215 ,845 ,845 ,845 ,845 ,845 ,845 ,845 ,845 ,189 ,189 ,189 ,189 ,189 ,189 ,189 ,189 ,189 ,861 ,861 ,861 ,861 ,861 ,861 ,861 ,350 ,350 ,645 ,645 ,645 ,617 ,617 ,617 ,302 ,302 ,302 ,302 ,444 ,444 ,444 ,444 ,444 ,444 ,444 ,444 ,444 ,444 ,406 ,406 ,406 ,406 ,406 ,406 ,406 ,406 ,163 ,163 ,163 ,163 ,163 ,163 ,163 ,793 ,793 ,793 ,793 ,793 ,793 ,793 ,793 ,257 ,257 ,257 ,257 ,257 ,257 ,257 ,385 ,385 ,385 ,385 ,680 ,680 ,680 ,680 ,680 ,680 ,680 ,680 ,286 ,286 ,286 ,286 ,286 ,286 ,487 ,487 ,487 ,416 ,416 ,416 ,416 ,416 ,416 ,416 ,532 ,532 ,532 ,532 ,532 ,660 ,660 ,639 ,639 ,639 ,639 ,639 ,639 ,639 ,639 ,582 ,582 ,582 ,582 ,582 ,582 ,582 ,582 ,582 ,582 ,238 ,238 ,238 ,238 ,265 ,265 ,265 ,265 ,265 ,622 ,622 ,622 ,999 ,999 ,999 ,999 ,999 ,999 ,999 ,999 ,999 ,532 ,532 ,532 ,532 ,532 ,532 ,532 ,532 ,936 ,936 ,936 ,936 ,936 ,936 ,373 ,373 ,373 ,373 ,373 ,373 ,373 ,363 ,363 ,363 ,363 ,363 ,363 ,363 ,292 ,292 ,292 ,292 ,292 ,516 ,516 ,110 ,110 ,110 ,110 ,110 ,110 ,110 ,110 ,761 ,761 ,761 ,761 ,761 ,598 ,598 ,598 ,598 ,598 ,537 ,537 ,537 ,994 ,994 ,935 ,935 ,30 ,30 ,30 ,30 ,139 ,139 ,139 ,139 ,139 ,139 ,139 ,139 ,269 ,269 ,531 ,531 ,786 ,786 ,786 ,786 ,786 ,786 ,786 ,786 ,786 ,326 ,326 ,326 ,326 ,326 ,326 ,326 ,326 ,476 ,476 ,476 ,476 ,476 ,476 ,367 ,367 ,367 ,367 ,367 ,367 ,367 ,367 ,786 ,786 ,786 ,37 ,37 ,565 ,565 ,565 ,324 ,324 ,324 ,324 ,324 ,324 ,324 ,324 ,382 ,382 ,382 ,382 ,382 ,382 ,382 ,382 ,642 ,642 ,642 ,642 ,642 ,531 ,531 ,531 ,531 ,531 ,531 ,531 ,531 ,531 ,531 ,459 ,459 ,459 ,459 ,459 ,459 ,459 ,514 ,514 ,514 ,911 ,911 ,930 ,930 ,930 ,930 ,930 ,930 ,930 ,930 ,264 ,264 ,264 ,264 ,264 ,264 ,264 ,264 ,264 ,264 ,239 ,239 ,239 ,217 ,217 ,217 ,217 ,217 ,217 ,217 ,217 ,217 ,217 ,784 ,784 ,784 ,784 ,784 ,784 ,126 ,126 ,126 ,126 ,126 ,126 ,126 ,126 ,126 ,865 ,865 ,865 ,865 ,865 ,252 ,252 ,252 ,390 ,390 ,390 ,390 ,390 ,390 ,390 ,390 ,390 ,138 ,138 ,138 ,138 ,138 ,138 ,138 ,138 ,732 ,732 ,732 ,732 ,732 ,732 ,732 ,732 ,210 ,210 ,210 ,210 ,210 ,197 ,197 ,197 ,457 ,457 ,457 ,457 ,457 ,457 ,457 ,457 ,457 ,457 ,198 ,198 ,198 ,198 ,198 ,715 ,715 ,715 ,715 ,715 ,715 ,715 ,762 ,762 ,762 ,762 ,762 ,762 ,762 ,762 ,762 ,548 ,548 ,548 ,548 ,368 ,368 ,368 ,722 ,722 ,722 ,722 ,722 ,722 ,661 ,661 ,661 ,661 ,661 ,519 ,519 ,519 ,519 ,519 ,519 ,519 ,519 ,519 ,])
expectedOutput = [(37, 2), (269, 2), (350, 2), (516, 2), (660, 2), (911, 2), (935, 2), (994, 2), (197, 3), (239, 3), (252, 3), (368, 3), (487, 3), (514, 3), (537, 3), (565, 3), (617, 3), (622, 3), (645, 3), (30, 4), (131, 4), (238, 4), (302, 4), (385, 4), (548, 4), (75, 5), (198, 5), (210, 5), (265, 5), (292, 5), (598, 5), (642, 5), (661, 5), (761, 5), (865, 5), (286, 6), (476, 6), (486, 6), (722, 6), (784, 6), (83, 7), (163, 7), (257, 7), (363, 7), (373, 7), (416, 7), (459, 7), (594, 7), (715, 7), (861, 7), (110, 8), (138, 8), (139, 8), (324, 8), (326, 8), (367, 8), (382, 8), (406, 8), (639, 8), (680, 8), (732, 8), (793, 8), (845, 8), (930, 8), (126, 9), (189, 9), (215, 9), (390, 9), (519, 9), (762, 9), (999, 9), (217, 10), (264, 10), (444, 10), (457, 10), (582, 10), (531, 12), (786, 12), (532, 13), (936, 14)]
print(actualOutput == expectedOutput)