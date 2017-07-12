def mro(cls):
    """
    Return ordering of superclass of cls
    This ordering was used when we want to access class instance atrribute

    `cls`: class type we want to resolve

    @raise `TypeError` if cannot resolution superclass order
    @return `list` of class
    """
    bases_cls = cls.__bases__
    mro_base_lists = [mro(base_cls) for base_cls in bases_cls]
    mro_list = [cls]
    while mro_base_lists:
        # find the good head
        # good head is head of a list which is not is tail of any list in mro_base_lists
        list_head = (x[0] for x in mro_base_lists)
        set_tails = set()
        for x in mro_base_lists:
            set_tails.update(x[1:])

        good_head = None
        for head in list_head:
            if head not in set_tails:
                good_head = head
                break

        # if cannot find good_head, raise TypeError
        if not good_head:
            raise TypeError
        else:
            # add to mro_list
            mro_list.append(good_head)

            # remove good_head in all list and add to mro_list
            for alist in mro_base_lists:
                try:
                    alist.remove(good_head)
                except Exception:
                    pass
            mro_base_lists = [x for x in mro_base_lists if x]
    return mro_list

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
class E(B, C): pass
class F(D, E): pass

def test_mro():
    assert mro(A) == [A]
    print "Test 1 passed"

    assert mro(B) == [B, A]
    print "Test 2 passed"

    assert mro(C) == [C, A]
    print "Test 3 passed"

    assert mro(D) == [D, B, C, A]
    print "Test 4 passed"

    assert mro(E) == [E, B, C, A]
    print "Test 5 passed"

    assert mro(F) == [F, D, E, B, C, A]
    print "Test 5 passed"

    try:
        mro(F)
    except Exception as e:
        assert isinstance(e, TypeError)
        print "Test 6 passed"


test_mro()
