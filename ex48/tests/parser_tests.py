from ex48.parser import *
from nose.tools import *


def test_peek():
    word_list = [('verb', 'cut'), ('noun', 'bag'), ('number', 1234)]
    assert_equal(peek(word_list), 'verb')


def test_match():
    # test empty
    word_list = []
    assert_equal(match(word_list, 'noun'), None)
    # test not expected
    word_list = [('verb', 'cut'), ('noun', 'bag'), ('number', 1234)]
    assert_equal(match(word_list, 'noun'), None)
    assert_equal(word_list, [('noun', 'bag'), ('number', 1234)])
    # test  expected
    word_list = [('verb', 'cut'), ('noun', 'bag'), ('number', 1234)]
    assert_equal(match(word_list, 'verb'), ('verb', 'cut'))
    assert_equal(word_list, [('noun', 'bag'), ('number', 1234)])


def test_parse_verb():
    word_list = [('stop', 'and'), ('stop', 'in'), ('verb', 'fight')]
    assert_equal(parse_verb(word_list), ('verb', 'fight'))
    word_list = [('stop', 'and'), ('stop', 'in'), ('stop', 'fight')]
    assert_raises(ParserError, parse_verb, word_list)


def test_parse_object():
    word_list = [('stop', 'and'), ('stop', 'in'), ('noun', 'king')]
    assert_equal(parse_object(word_list), ('noun', 'king'))
    word_list = [('stop', 'and'), ('stop', 'in'), ('direction', 'left')]
    assert_equal(parse_object(word_list), ('direction', 'left'))
    word_list = [('stop', 'and'), ('stop', 'in'), ('stop', 'left')]
    assert_raises(ParserError, parse_object, word_list)


def test_parse_subject():
    word_list = [('verb', 'fights'), ('stop', 'and'), ('stop', 'and'), ('noun', 'king')]
    sentence = parse_subject(word_list, ('noun', 'player'))
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.object, 'king')
    assert_equal(sentence.verb, 'fights')
    word_list = [('noun', 'fights'), ('stop', 'and'), ('stop', 'and'), ('noun', 'king')]
    assert_raises(ParserError, parse_subject, word_list, ('noun', 'player'))
    word_list = [('verb', 'fights'), ('stop', 'and'), ('stop', 'and'), ('stop', 'and')]
    assert_raises(ParserError, parse_subject, word_list, ('noun', 'player'))


def test_parse_sentence():
    word_list = [('noun', 'I'), ('verb', 'fight'), ('stop', 'and'), ('stop', 'and'), ('noun', 'king')]
    sentence = parse_sentence(word_list)
    assert_equal(sentence.subject, 'I')
    assert_equal(sentence.object, 'king')
    assert_equal(sentence.verb, 'fight')
    word_list = [('verb', 'fights'), ('stop', 'and'), ('stop', 'and'), ('noun', 'king')]
    sentence = parse_sentence(word_list)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.object, 'king')
    assert_equal(sentence.verb, 'fights')
    word_list = [('verb', 'fights'), ('stop', 'and'), ('stop', 'and'), ('stop', 'and')]
    assert_raises(ParserError, parse_sentence, word_list)
    word_list = [('noun', 'fights'), ('stop', 'and'), ('stop', 'and'), ('noun', 'and')]
    assert_raises(ParserError, parse_sentence, word_list)

