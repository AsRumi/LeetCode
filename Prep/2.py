"""
==========================================================================
 DEFAULTDICT PLAYGROUND
==========================================================================
How to use this file:
  1. Read PART 0 (short notes). Run the file once:  python Prep/2.py
  2. PART 1: predict outputs WITHOUT running the snippet. Write your guess
     into GUESS_n. Then run the file -- the scoreboard tells you if you were
     right and shows the real answer.
  3. PARTS 2-4: replace each `raise NotImplementedError` with your code.
     Re-run the file; every exercise shows TODO / PASS / FAIL.
  4. Stuck? Hints are at the very bottom. Try for a while first.

Rule for this file: don't use Counter or heapq yet -- those are the next
topics. The point is to feel what defaultdict alone can do.
"""
from collections import defaultdict


# ==========================================================================
# PART 0 -- THE NOTES (read, don't edit)
# ==========================================================================
#
# defaultdict is a dict subclass. The ONLY difference from a normal dict:
#   when you read d[key] and key is missing, it calls default_factory()
#   with NO arguments, STORES the result under key, and returns it.
#
#   d = defaultdict(list)      # factory = list   -> missing key gets []
#   d = defaultdict(int)       # factory = int    -> missing key gets 0
#   d = defaultdict(set)       # factory = set    -> missing key gets set()
#   d = defaultdict(lambda: -1)  # any zero-arg callable works
#
# Why it matters for LeetCode -- it removes this boilerplate:
#
#   if key not in groups:          groups = defaultdict(list)
#       groups[key] = []     -->   groups[key].append(x)
#   groups[key].append(x)
#
# Things that DO trigger the factory:      d[key]   (reading OR += OR .append)
# Things that do NOT trigger the factory:  key in d,  d.get(key),  len(d),
#                                          d.pop(key) (raises KeyError), iteration
#
# The magic hook underneath: dict.__getitem__ calls self.__missing__(key)
# when the key is absent. defaultdict just implements __missing__.
# (You'll build this yourself in PART 4.)


# ==========================================================================
# PART 1 -- PREDICT THE OUTPUT
# ==========================================================================
# Don't run these in your head with "it's probably X" -- trace them.
# Replace the `...` with your guess (a value). If you think the snippet
# raises an exception, write the exception name as a string, e.g. "KeyError".

def p1():
    d = defaultdict(int)
    d["a"] += 1
    d["b"]
    return len(d)

GUESS_1 = 2


def p2():
    d = defaultdict(list)
    "x" in d
    d.get("y")
    return len(d)

GUESS_2 = 0


def p3():
    d = defaultdict(list)
    d["k"].append(1)
    d["k"].append(2)
    d["j"]
    return dict(d)

GUESS_3 = {"k": [1, 2],
           "j": []}


def p4():
    d = defaultdict(set)
    d["a"].add(1)
    d["a"].add(1)
    d["b"].add(2)
    return len(d["a"]) + len(d)

GUESS_4 = 3


def p5():
    # The classic bug: "checking" a value creates the key.
    counts = defaultdict(int, {"a": 3})
    for ch in "abc":
        if counts[ch] > 0:
            pass
    return sorted(counts)

GUESS_5 = ['a', 'b', 'c'] # Only returns the keys, not the values.


def p6():
    d = defaultdict()          # no factory given
    return d["x"]

GUESS_6 = 'KeyError' # Without a factory, it does not default to int.


def p7():
    d = defaultdict(defaultdict(int))
    return d

GUESS_7 = 'TypeError'


def p8():
    g = defaultdict(lambda: defaultdict(int))
    g["u"]["v"] += 5
    g["u"]["w"]
    g["x"]
    return (len(g), len(g["u"]))

GUESS_8 = (2, 2)


def p9():
    d = defaultdict(int)
    d["a"] += 1
    return d == {"a": 1}

GUESS_9 = True


def p10():
    d = defaultdict(list)
    d["a"].append(1)
    d.default_factory = None   # you can swap/remove the factory later
    return d["zzz"]

GUESS_10 = 'KeyError' # Once you remove the factory default, every key that does not exist throws a KeyError.


def p11():
    # Iterating while the dict might grow.
    d = defaultdict(int, {"a": 1, "b": 2})
    for k in d:
        d[k + "!"]
    return "done"

GUESS_11 = "RuntimeError"


# ==========================================================================
# PART 2 -- WARM-UPS (one defaultdict each, no `if key not in d`)
# ==========================================================================

def group_by_length(words):
    """
    Return a dict: length -> list of words with that length, in input order.
    group_by_length(["hi", "yo", "cat", "a", "dog"])
      -> {2: ["hi", "yo"], 3: ["cat", "dog"], 1: ["a"]}
    """
    result = defaultdict(list) # List because what do you want the default value of the key to be if the key does not exist?
    # An empty list. Therefore defaultdict(list)
    
    for word in words:
        result[len(word)].append(word)
    
    return result


def char_count(s):
    """
    Count each character. Use defaultdict(int), NOT Counter.
    char_count("banana") -> {"b": 1, "a": 3, "n": 2}
    """
    result = defaultdict(int)
    for char in s: 
        result[char] += 1
    
    return result


def invert_dict(d):
    """
    Many keys can share a value. Return value -> list of keys (input order).
    invert_dict({"alice": "NY", "bob": "LA", "carol": "NY"})
      -> {"NY": ["alice", "carol"], "LA": ["bob"]}
    """
    result = defaultdict(list)
    
    for key, value in d.items():
        result[value].append(key)
    
    return result


def build_adjacency(edges, directed=False):
    """
    edges: list of (u, v) pairs. Return node -> list of neighbors.
    EVERY node that appears in edges must be a key, even if it has no
    outgoing edges (this matters in graph problems -- think about how the
    "gotcha" from p1/p5 can be used on purpose here).

    build_adjacency([(1, 2), (2, 3)])                -> {1: [2], 2: [1, 3], 3: [2]}
    build_adjacency([(1, 2), (2, 3)], directed=True) -> {1: [2], 2: [3], 3: []}
    """
    
    graph = defaultdict(list)
    
    for source, dest in edges:
        graph[dest] # simply query it so the list is built.
        graph[source].append(dest)
        if not directed:
            graph[dest].append(source)
            
    return graph


# ==========================================================================
# PART 3 -- LEETCODE MEDIUMS WHERE DEFAULTDICT IS THE KEY IDEA
# ==========================================================================

def group_anagrams(strs):
    """
    LC 49. Group Anagrams.
    ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]
    (any order of groups / within groups is fine)
    Think: what can be a dict KEY that is identical for all anagrams?
    Bonus: do it once with a sorted-string key, once with a 26-count tuple key.
    """
        
    result = defaultdict(list)
    
    for word in strs:
        result["".join(sorted(word))].append(word)
    
    return result.values()


def can_finish(num_courses, prerequisites):
    """
    LC 207. Course Schedule.
    prerequisites[i] = [a, b] means "to take a you must first take b".
    Return True if all courses can be finished (i.e. no cycle).
    can_finish(2, [[1, 0]])          -> True
    can_finish(2, [[1, 0], [0, 1]])  -> False
    Use defaultdict(list) for the graph and defaultdict(int) for in-degrees
    (or a list for in-degrees -- your call, but try the dict once).
    """
    
    
        
    # check if the graph has a cycle or not
    
    
    raise NotImplementedError


def subarray_sum(nums, k):
    """
    LC 560. Subarray Sum Equals K. Count contiguous subarrays summing to k.
    subarray_sum([1, 1, 1], 2) -> 2
    subarray_sum([1, 2, 3], 3) -> 2
    Must be O(n). Negative numbers allowed (so sliding window won't work).
    """
    raise NotImplementedError


def top_k_frequent(nums, k):
    """
    LC 347. Top K Frequent Elements. Return the k most frequent values
    (any order). No Counter, no heapq, no sorting the counts.
    Aim for O(n) with "bucket sort": frequency -> list of numbers.
    top_k_frequent([1, 1, 1, 2, 2, 3], 2) -> [1, 2]
    """
    
    
    
    raise NotImplementedError


class TimeMap:
    """
    LC 981. Time Based Key-Value Store.
    set(key, value, timestamp): timestamps for a key arrive strictly increasing.
    get(key, timestamp): value with the largest stored timestamp <= timestamp,
                         or "" if none.
    Store: key -> list of (timestamp, value). Use binary search in get.
    Challenge: get() on an unknown key must NOT add that key to your store.
    """

    def __init__(self):
        raise NotImplementedError

    def set(self, key, value, timestamp):
        raise NotImplementedError

    def get(self, key, timestamp):
        raise NotImplementedError


class Trie:
    """
    LC 208. Implement Trie -- using a RECURSIVE defaultdict.
    A node is a dict: char -> child node. A child node is... the same kind
    of thing. So the factory needs to produce something that produces itself.
    Mark end-of-word with the special key "$" (e.g. node["$"] = True).

    Requirements:
      - The root must be stored in self.root
      - search / starts_with must NOT create new nodes (the tests check!)
    """

    def __init__(self):
        raise NotImplementedError

    def insert(self, word):
        raise NotImplementedError

    def search(self, word):
        raise NotImplementedError

    def starts_with(self, prefix):
        raise NotImplementedError


# ==========================================================================
# PART 4 -- UNDER THE HOOD: BUILD YOUR OWN DEFAULTDICT
# ==========================================================================

class MyDefaultDict(dict):
    """
    Re-implement defaultdict by subclassing dict and defining __missing__.
    - MyDefaultDict(list), MyDefaultDict(int, {"a": 5}) should both work
      (extra args are passed through to dict's constructor).
    - With default_factory=None, a missing key raises KeyError.
    - .get() and `in` must not create keys -- notice you get that for free.
      Why? Which dict method calls __missing__ and which don't?
    """

    def __init__(self, default_factory=None, *args, **kwargs):
        raise NotImplementedError

    def __missing__(self, key):
        raise NotImplementedError


# ==========================================================================
# SCOREBOARD -- no need to edit below (except peeking at hints, last resort)
# ==========================================================================

def _run_predictions():
    print("PART 1 -- predictions")
    for i in range(1, 12):
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
        print(f"  {name:<18} PASS")
    except NotImplementedError:
        print(f"  {name:<18} TODO")
    except AssertionError as e:
        print(f"  {name:<18} FAIL  {e}")
    except Exception as e:
        print(f"  {name:<18} ERROR {type(e).__name__}: {e}")


def _eq(got, want, label=""):
    assert got == want, f"{label} got {got!r}, want {want!r}"


def _t_group_by_length():
    _eq(dict(group_by_length(["hi", "yo", "cat", "a", "dog"])),
        {2: ["hi", "yo"], 3: ["cat", "dog"], 1: ["a"]})
    _eq(dict(group_by_length([])), {})


def _t_char_count():
    _eq(dict(char_count("banana")), {"b": 1, "a": 3, "n": 2})
    _eq(dict(char_count("")), {})


def _t_invert_dict():
    _eq(dict(invert_dict({"alice": "NY", "bob": "LA", "carol": "NY"})),
        {"NY": ["alice", "carol"], "LA": ["bob"]})


def _t_build_adjacency():
    _eq(dict(build_adjacency([(1, 2), (2, 3)])), {1: [2], 2: [1, 3], 3: [2]}, "undirected:")
    _eq(dict(build_adjacency([(1, 2), (2, 3)], directed=True)), {1: [2], 2: [3], 3: []}, "directed:")


def _t_group_anagrams():
    norm = lambda groups: sorted(sorted(g) for g in groups)
    _eq(norm(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])),
        norm([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]))
    _eq(norm(group_anagrams([""])), [[""]])
    _eq(norm(group_anagrams(["a"])), [["a"]])


def _t_can_finish():
    _eq(can_finish(2, [[1, 0]]), True, "(2, [[1,0]])")
    _eq(can_finish(2, [[1, 0], [0, 1]]), False, "(2, [[1,0],[0,1]])")
    _eq(can_finish(5, [[1, 0], [2, 1], [3, 2], [4, 3]]), True, "chain:")
    _eq(can_finish(3, [[0, 1], [1, 2], [2, 0]]), False, "3-cycle:")
    _eq(can_finish(3, []), True, "no prereqs:")


def _t_subarray_sum():
    _eq(subarray_sum([1, 1, 1], 2), 2, "[1,1,1],2:")
    _eq(subarray_sum([1, 2, 3], 3), 2, "[1,2,3],3:")
    _eq(subarray_sum([1, -1, 0], 0), 3, "[1,-1,0],0:")
    _eq(subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7), 4, "long:")


def _t_top_k_frequent():
    _eq(sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)), [1, 2])
    _eq(sorted(top_k_frequent([1], 1)), [1])
    _eq(sorted(top_k_frequent([4, 4, 5, 5, 5, 6, 6, 6, 6], 2)), [5, 6])


def _t_timemap():
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    _eq(tm.get("foo", 1), "bar", "get(foo,1):")
    _eq(tm.get("foo", 3), "bar", "get(foo,3):")
    tm.set("foo", "bar2", 4)
    _eq(tm.get("foo", 4), "bar2", "get(foo,4):")
    _eq(tm.get("foo", 5), "bar2", "get(foo,5):")
    _eq(tm.get("foo", 0), "", "get(foo,0):")
    _eq(tm.get("nope", 1), "", "get(nope,1):")


def _t_trie():
    t = Trie()
    t.insert("apple")
    _eq(t.search("apple"), True, "search(apple):")
    _eq(t.search("app"), False, "search(app):")
    _eq(t.starts_with("app"), True, "starts_with(app):")
    t.insert("app")
    _eq(t.search("app"), True, "search(app) after insert:")
    _eq(t.search("zzz"), False, "search(zzz):")
    _eq(t.starts_with("zq"), False, "starts_with(zq):")
    assert "z" not in t.root, "search/starts_with created nodes in the trie!"
    assert "p" not in t.root["a"]["p"]["p"]["l"], "search created a node under 'appl'"


def _t_my_defaultdict():
    d = MyDefaultDict(list)
    d["a"].append(1)
    _eq(d, {"a": [1]}, "append on missing key:")
    _eq(d.get("b"), None, ".get(missing):")
    assert "b" not in d, ".get() should not create keys"
    _eq(MyDefaultDict(int, {"a": 5})["a"], 5, "init with data:")
    c = MyDefaultDict(int)
    for ch in "aab":
        c[ch] += 1
    _eq(c, {"a": 2, "b": 1}, "counting:")
    try:
        MyDefaultDict()["x"]
    except KeyError:
        pass
    else:
        raise AssertionError("factory=None should raise KeyError on missing key")


if __name__ == "__main__":
    _run_predictions()
    print("\nPART 2 -- warm-ups")
    _check("group_by_length", _t_group_by_length)
    _check("char_count", _t_char_count)
    _check("invert_dict", _t_invert_dict)
    _check("build_adjacency", _t_build_adjacency)
    print("\nPART 3 -- LeetCode mediums")
    _check("group_anagrams", _t_group_anagrams)
    _check("can_finish", _t_can_finish)
    _check("subarray_sum", _t_subarray_sum)
    _check("top_k_frequent", _t_top_k_frequent)
    _check("TimeMap", _t_timemap)
    _check("Trie", _t_trie)
    print("\nPART 4 -- under the hood")
    _check("MyDefaultDict", _t_my_defaultdict)


# ==========================================================================
# HINTS (one nudge each -- not solutions)
# ==========================================================================
# build_adjacency : For the directed case, a bare `adj[v]` line is enough to
#                   make sure v exists. Normally a bug, here a feature.
# group_anagrams  : Lists can't be dict keys (unhashable). Strings and tuples can.
# can_finish      : Kahn's algorithm -- start a queue with every course whose
#                   in-degree is 0. Careful: courses with no edges never appear
#                   in your defaultdict unless you put them there; loop over
#                   range(num_courses) instead of over the dict.
# subarray_sum    : prefix_count[s] = how many prefixes summed to s so far.
#                   What prefix sum would you need to have seen before to end a
#                   subarray summing to k right here? Don't forget the empty prefix.
# top_k_frequent  : A frequency can be at most len(nums). Walk buckets from
#                   high frequency down.
# TimeMap         : `bisect` works on a list of tuples. What tuple compares as
#                   "just after every (timestamp, anything)"? Also: d[key] vs
#                   d.get(key, []) in get().
# Trie            : def node(): return defaultdict(node)   -- a function can
#                   reference itself by name because the lookup happens at call
#                   time. For lookups, walk with `in` checks, not node[ch].
# MyDefaultDict   : __missing__ should do three things: check the factory,
#                   build a value, store it. Then return it.
