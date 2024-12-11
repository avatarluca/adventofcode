% ---------------------------------- Regle ----------------------------------
% wenn 0, denn durch 1 ersetze
use_stone_rule(0, Count, [1-Count]).

% wenn gradi azahl ziffere, denn split
use_stone_rule(Stone, Count, [Left-Count, Right-Count]) :-
    Stone > 0,
    number_codes(Stone, Codes),
    length(Codes, Len),
    Len mod 2 =:= 0, % isch grad?
    HalfLen is Len // 2,
    length(LeftCodes, HalfLen),
    append(LeftCodes, RightCodes, Codes),
    number_codes(Left, LeftCodes),
    number_codes(Right, RightCodes).

% sonst
use_stone_rule(Stone, Count, [NewStone-Count]) :-
    Stone > 0,
    NewStone is Stone * 2024.
% ---------------------------------- Regle ----------------------------------


use_for_all_stones([], Result, Result).
use_for_all_stones([Stone-Count | Rest], Acc, Result) :-
    use_stone_rule(Stone, Count, Transformed),
    update_counts(Transformed, Acc, NewAcc),
    use_for_all_stones(Rest, NewAcc, Result).

update_counts([], Acc, Acc).
update_counts([Stone-Count | Rest], Acc, Result) :-
    ( select(Stone-OldCount, Acc, TempAcc) ->
        NewCount is OldCount + Count,
        update_counts(Rest, [Stone-NewCount | TempAcc], Result)
    ;   update_counts(Rest, [Stone-Count | Acc], Result)
    ).

blink(Stones, 0, Stones).
blink(Stones, Blinks, Result) :-
    Blinks > 0,
    use_for_all_stones(Stones, [], NewStones),
    NewBlinks is Blinks - 1,
    blink(NewStones, NewBlinks, Result).

count(Stones, Blinks, Count) :-
    blink(Stones, Blinks, FinalStones),
    findall(C, member(S-C, FinalStones), Counts),
    sum_list(Counts, Count).

% ?- count([64599-1, 31-1, 674832-1, 2659361-1, 1-1, 0-1, 8867-1, 321-1], 25, Count) % Stone - Count Paar
