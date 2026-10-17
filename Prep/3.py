"""
==========================================================================
 COUNTER PLAYGROUND
==========================================================================
How to use this file:
  1. Read PART 0. Run the file once:  python Prep/3.py
  2. PART 1: predict outputs WITHOUT running the snippet. Write your guess
     into GUESS_n. Run the file -- the scoreboard checks you.
  3. PARTS 2-4: replace each `raise NotImplementedError` with your code.
  4. Hints at the very bottom, one nudge each.

Rule for this file: no heapq yet. Counter's own methods are the point --
if you catch yourself writing a manual counting loop, look for the
Counter method that already does it.
"""
from collections import Counter


# ==========================================================================
# PART 0 -- THE NOTES (read, don't edit)
# ==========================================================================
#
# Counter is a dict subclass: element -> count.
#
#   Counter("banana")                 -> {'a': 3, 'n': 2, 'b': 1}
#   Counter(["hi", "hi", "yo"])       -> {'hi': 2, 'yo': 1}
#   Counter({"a": 2, "b": 1})         -> from a mapping
#   Counter(a=2, b=1)                 -> from keyword args
#
# Missing keys:  c["zzz"] returns 0 and does NOT insert the key.
#                (Compare with defaultdict(int), which DOES insert.)
#
# The methods you'll actually use on LeetCode:
#   c.most_common(k)     list of (elem, count), highest first. Ties keep
#                        first-seen order. No argument = all of them.
#   c.update(iterable)   ADD counts   (iterable of elements, or a mapping)
#   c.subtract(iterable) SUBTRACT counts -- results can go to 0 or negative
#   c.elements()         iterator repeating each elem `count` times (skips <= 0)
#   c.total()            sum of all counts (Python 3.10+)
#
# Multiset arithmetic -- each returns a NEW Counter and DROPS counts <= 0:
#   c1 + c2    add counts
#   c1 - c2    subtract counts, keep only positives
#   c1 & c2    min of each count   (intersection)
#   c1 | c2    max of each count   (union)
#   +c         just "drop non-positive counts"
#
# Comparisons (3.10+): missing keys count as 0.
#   c1 == c2   same multiset         c1 <= c2   c1 fits inside c2
#
# Zero counts don't disappear by themselves: after c["a"] -= 1 hits 0,
# "a" is still a key. Use `del c["a"]` if you need it gone (e.g. when you
# rely on len(c) as "number of distinct elements in my window").


# ==========================================================================
# PART 1 -- PREDICT THE OUTPUT
# ==========================================================================
# Replace `...` with your guess. If it raises, write the exception name
# as a string, e.g. "TypeError".

def p1():
    c = Counter("banana")
    c["z"]
    return len(c)

GUESS_1 = 3


def p2():
    c = Counter("banana")
    return c["z"] + c["a"]

GUESS_2 = 3


def p3():
    return dict(Counter("aab") + Counter("abb"))

GUESS_3 = {"a": 3,
           "b": 3}


def p4():
    c = Counter(a=3, b=1)
    c.subtract(Counter(a=1, b=2))
    return dict(c)

GUESS_4 = {"a": 2, "b": -1}


def p5():
    return dict(Counter(a=3, b=1) - Counter(a=1, b=2))

GUESS_5 = {"a": 2}


def p6():
    x = Counter(a=3, b=1)
    y = Counter(a=1, b=2, c=5)
    return (dict(x & y), dict(x | y))

GUESS_6 = ({"a": 1,
            "b": 1}, 
           {"a": 3,
            "b": 2,
            "c": 5})


def p7():
    # Watch the tie between 'b' and 'r'.
    return Counter("abracadabra").most_common(3)

GUESS_7 = [('a', 5), ('b', 2), ('r', 2)]


def p8():
    c = Counter(["hi", "hi", "yo"])
    c.update("hi")
    return dict(c)

GUESS_8 = {'hi': 2, 'yo': 1, 'h': 1, 'i': 1}


def p9():
    return sorted(Counter(a=2, b=0, c=-1).elements())

GUESS_9 = ['a', 'a']


def p10():
    c = Counter(a=2, b=-1)
    return (dict(+c), c.total())

GUESS_10 = ({'a': 2}, 
            1)


def p11():
    return (Counter(a=1, b=0) == Counter(a=1),
            Counter("ab") <= Counter("aabc"),
            Counter("abb") <= Counter("ab"))

GUESS_11 = (True, True, False)


def p12():
    c = Counter("aab")
    c["a"] -= 2
    return ("a" in c, len(c))

GUESS_12 = (True, 2)


def p13():
    c = Counter("hello")
    return c.most_common()[-1]

GUESS_13 = ('o', 1)


# ==========================================================================
# PART 2 -- WARM-UPS (most are one or two lines with the right method)
# ==========================================================================

def is_anagram(s, t):
    """
    LC 242. True if t is an anagram of s.
    is_anagram("anagram", "nagaram") -> True
    """
    return Counter(s) == Counter(t)


def can_construct(ransom_note, magazine):
    """
    LC 383. Can ransom_note be built from magazine's letters (each used once)?
    can_construct("aa", "aab") -> True
    can_construct("aa", "ab")  -> False
    Try it two ways: with `-`, and with `<=`.
    """
    return Counter(ransom_note) <= Counter(magazine)


def first_unique_char(s):
    """
    LC 387. Index of the first non-repeating character, or -1.
    first_unique_char("loveleetcode") -> 2
    """
    charCounter = Counter(s)
    sorted_by_freq = sorted(charCounter.items(), key=lambda item: item[1], reverse=True)
    i = 0
    while i < len(sorted_by_freq) and sorted_by_freq[i][1] > 1:
        i += 1
    if i == len(sorted_by_freq):
        return -1
    else: 
        return s.find(sorted_by_freq[i][0])


def k_most_common_words(text, k):
    """
    Lowercase the text, split on whitespace, return the k most common words
    as a list of (word, count). Ties: whichever word appeared first wins.
    k_most_common_words("The cat and the hat AND the bat", 2)
      -> [("the", 3), ("and", 2)]
    """
    
    raise NotImplementedError


def common_chars(words):
    """
    LC 1002. Characters that appear in ALL words, including duplicates.
    common_chars(["bella", "label", "roller"]) -> ["e", "l", "l"]  (any order)
    Which multiset operator is "keep the minimum count"?
    """
    raise NotImplementedError


# ==========================================================================
# PART 3 -- LEETCODE MEDIUMS WHERE COUNTER IS THE KEY IDEA
# ==========================================================================

def min_steps_to_anagram(s, t):
    """
    LC 1347. Minimum Number of Steps to Make Two Strings Anagram.
    One step = replace any character of t with any character.
    min_steps_to_anagram("leetcode", "practice") -> 5
    There's a one-liner hiding here with `-` and .total().
    """
    raise NotImplementedError


def find_anagrams(s, p):
    """
    LC 438. Find All Anagrams in a String. Return start indices of p's
    anagrams in s.
    find_anagrams("cbaebabacd", "abc") -> [0, 6]
    find_anagrams("abab", "ab")        -> [0, 1, 2]
    Keep ONE Counter for the window and slide it -- don't rebuild
    Counter(s[i:i+len(p)]) every step (that's O(n * m)).
    """
    raise NotImplementedError


def least_interval(tasks, n):
    """
    LC 621. Task Scheduler. Same task needs n idle slots between runs.
    Return the minimum number of time units.
    least_interval(["A","A","A","B","B","B"], 2) -> 8   (A B _ A B _ A B)
    Only two numbers matter: the highest frequency, and how many tasks
    share that highest frequency.
    """
    raise NotImplementedError


def is_n_straight_hand(hand, group_size):
    """
    LC 846. Hand of Straights. Can the cards be split into groups of
    `group_size` consecutive numbers?
    is_n_straight_hand([1,2,3,6,2,3,4,7,8], 3) -> True  ([1,2,3],[2,3,4],[6,7,8])
    is_n_straight_hand([1,2,3,4,5], 4)         -> False
    Greedy: the smallest card left MUST start a group.
    """
    raise NotImplementedError


def top_k_frequent_words(words, k):
    """
    LC 692. Top K Frequent Words -- BRIDGE to the next topic.
    Sort by frequency (high first), ties broken ALPHABETICALLY.
    top_k_frequent_words(["i","love","leetcode","i","love","coding"], 2)
      -> ["i", "love"]
    most_common() alone won't do the tie-break (it uses first-seen order).
    You're allowed `sorted` with a key here. What key gives
    "count descending, then word ascending"?
    """
    raise NotImplementedError


# ==========================================================================
# PART 4 -- UNDER THE HOOD: BUILD YOUR OWN COUNTER
# ==========================================================================

class MiniCounter(dict):
    """
    A small Counter clone. Subclass dict; don't use collections.Counter.
      - MiniCounter() and MiniCounter("aab") both work (iterable of elements).
      - c[missing] returns 0 and must NOT insert the key.
        (2.py's MyDefaultDict stored the value in __missing__. What changes?)
      - update(iterable): add 1 per element.
      - most_common(n=None): list of (elem, count), highest first, ties in
        insertion order, first n only if n is given.
        Hint-word: "stable".
      - a + b: NEW MiniCounter with summed counts, keeping only counts > 0.
    """

    def __init__(self, iterable=()):
        raise NotImplementedError

    def __missing__(self, key):
        raise NotImplementedError

    def update(self, iterable):
        raise NotImplementedError

    def most_common(self, n=None):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError


# ==========================================================================
# SCOREBOARD -- no need to edit below (except peeking at hints, last resort)
# ==========================================================================

N_PREDICTIONS = 13


def _run_predictions():
    print("PART 1 -- predictions")
    for i in range(1, N_PREDICTIONS + 1):
        fn = globals()[f"p{i}"]
        guess = globals()[f"GUESS_{i}"]
        try:
            actual = fn()
        except Exception as e:
            actual = type(e).__name__
        if guess is ...:
            print(f"  p{i:<3} TODO")
        elif guess == actual:
            print(f"  p{i:<3} PASS")
        else:
            print(f"  p{i:<3} FAIL  you said {guess!r}, actual {actual!r}")


def _check(name, test):
    try:
        test()
        print(f"  {name:<22} PASS")
    except NotImplementedError:
        print(f"  {name:<22} TODO")
    except AssertionError as e:
        print(f"  {name:<22} FAIL  {e}")
    except Exception as e:
        print(f"  {name:<22} ERROR {type(e).__name__}: {e}")


def _eq(got, want, label=""):
    assert got == want, f"{label} got {got!r}, want {want!r}"


def _t_is_anagram():
    _eq(is_anagram("anagram", "nagaram"), True, "anagram/nagaram:")
    _eq(is_anagram("rat", "car"), False, "rat/car:")
    _eq(is_anagram("aab", "ab"), False, "aab/ab:")


def _t_can_construct():
    _eq(can_construct("a", "b"), False, "a/b:")
    _eq(can_construct("aa", "ab"), False, "aa/ab:")
    _eq(can_construct("aa", "aab"), True, "aa/aab:")
    _eq(can_construct("", "x"), True, "empty note:")


def _t_first_unique_char():
    _eq(first_unique_char("leetcode"), 0, "leetcode:")
    _eq(first_unique_char("loveleetcode"), 2, "loveleetcode:")
    _eq(first_unique_char("aabb"), -1, "aabb:")


def _t_k_most_common_words():
    _eq(k_most_common_words("The cat and the hat AND the bat", 2), [("the", 3), ("and", 2)])
    _eq(k_most_common_words("b a b a c", 1), [("b", 2)], "tie -> first seen:")


def _t_common_chars():
    _eq(sorted(common_chars(["bella", "label", "roller"])), ["e", "l", "l"])
    _eq(sorted(common_chars(["cool", "lock", "cook"])), ["c", "o"])
    _eq(sorted(common_chars(["abc", "xyz"])), [])


def _t_min_steps():
    _eq(min_steps_to_anagram("bab", "aba"), 1, "bab/aba:")
    _eq(min_steps_to_anagram("leetcode", "practice"), 5, "leetcode/practice:")
    _eq(min_steps_to_anagram("anagram", "mangaar"), 0, "anagram/mangaar:")


def _t_find_anagrams():
    _eq(find_anagrams("cbaebabacd", "abc"), [0, 6], "cbaebabacd/abc:")
    _eq(find_anagrams("abab", "ab"), [0, 1, 2], "abab/ab:")
    _eq(find_anagrams("a", "ab"), [], "p longer than s:")
    _eq(find_anagrams("aaaa", "aa"), [0, 1, 2], "aaaa/aa:")


def _t_least_interval():
    _eq(least_interval(["A", "A", "A", "B", "B", "B"], 2), 8, "AAABBB n=2:")
    _eq(least_interval(["A", "A", "A", "B", "B", "B"], 0), 6, "AAABBB n=0:")
    _eq(least_interval(["A", "C", "A", "B", "D", "B"], 1), 6, "ACABDB n=1:")
    _eq(least_interval(list("AAAAAABCDEFG"), 2), 16, "AAAAAABCDEFG n=2:")


def _t_straight_hand():
    _eq(is_n_straight_hand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True, "example 1:")
    _eq(is_n_straight_hand([1, 2, 3, 4, 5], 4), False, "example 2:")
    _eq(is_n_straight_hand([1, 1, 2, 2, 3, 3], 3), True, "doubles:")
    _eq(is_n_straight_hand([1, 2, 4, 5], 2), True, "gap between groups:")
    _eq(is_n_straight_hand([1, 3], 2), False, "not consecutive:")


def _t_top_k_words():
    _eq(top_k_frequent_words(["i", "love", "leetcode", "i", "love", "coding"], 2), ["i", "love"])
    _eq(top_k_frequent_words(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
        ["the", "is", "sunny", "day"])
    _eq(top_k_frequent_words(["b", "a", "c"], 2), ["a", "b"], "all ties -> alphabetical:")


def _t_mini_counter():
    c = MiniCounter("abracadabra")
    _eq(dict(c), {"a": 5, "b": 2, "r": 2, "c": 1, "d": 1}, "construct:")
    _eq(c["z"], 0, "missing key value:")
    assert "z" not in c, "c[missing] inserted the key"
    _eq(c.most_common(3), [("a", 5), ("b", 2), ("r", 2)], "most_common(3):")
    _eq(len(c.most_common()), 5, "most_common() length:")
    c.update("zz")
    _eq(c["z"], 2, "after update:")
    _eq(dict(MiniCounter()), {}, "empty:")
    s = MiniCounter("ab") + MiniCounter("bc")
    assert isinstance(s, MiniCounter), "a + b should return a MiniCounter"
    _eq(dict(s), {"a": 1, "b": 2, "c": 1}, "a + b:")
    neg = MiniCounter("a")
    neg["b"] = -3
    _eq(dict(neg + MiniCounter("b")), {"a": 1}, "+ drops counts <= 0:")


if __name__ == "__main__":
    _run_predictions()
    print("\nPART 2 -- warm-ups")
    _check("is_anagram", _t_is_anagram)
    _check("can_construct", _t_can_construct)
    _check("first_unique_char", _t_first_unique_char)
    _check("k_most_common_words", _t_k_most_common_words)
    _check("common_chars", _t_common_chars)
    print("\nPART 3 -- LeetCode mediums")
    _check("min_steps_to_anagram", _t_min_steps)
    _check("find_anagrams", _t_find_anagrams)
    _check("least_interval", _t_least_interval)
    _check("is_n_straight_hand", _t_straight_hand)
    _check("top_k_frequent_words", _t_top_k_words)
    print("\nPART 4 -- under the hood")
    _check("MiniCounter", _t_mini_counter)


# ==========================================================================
# HINTS (one nudge each -- not solutions)
# ==========================================================================
# can_construct   : `Counter(a) - Counter(b)` is empty exactly when... ?
#                   An empty Counter is falsy.
# first_unique_char: Count first, then walk the string (not the Counter)
#                   with enumerate.
# common_chars    : functools.reduce(operator, iterable) folds a list with an
#                   operator. Then .elements() turns counts back into chars.
# min_steps       : Which characters of s are "missing" from t? Each missing
#                   char costs exactly one replacement.
# find_anagrams   : Each step: add s[i] to the window, remove s[i - len(p)].
#                   Compare window == need. (Since 3.10, zero counts don't break
#                   ==, but on older Pythons / other languages you'd del zero keys.)
# least_interval  : Picture (max_freq - 1) full "frames" of length n + 1, then
#                   one last partial frame. Answer can't be less than len(tasks).
# straight_hand   : Walk sorted(count) keys; when a card still has count c > 0,
#                   it starts c groups at once -- subtract c from the next
#                   group_size - 1 cards. If any would go negative, fail.
# top_k_words     : key=lambda w: (-count[w], w). Negating a number flips the
#                   order of just that part of the tuple.
# MiniCounter     : __missing__ just returns 0 (no assignment). For
#                   most_common, sorted() is stable: equal keys keep their
#                   original (insertion) order.
