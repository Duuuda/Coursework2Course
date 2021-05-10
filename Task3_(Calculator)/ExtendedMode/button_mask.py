from Utils import b


button_mask = (
    (None,                  None,                 None,                None,                     None),
    (None,                  None,                 None,                None,                     None),
    (None,                  None,                 None,                None,                     None),
    (b('change_mode', '≡'), b('change_id', '<>'), None,                b('backspace', '←'),      b('clear', 'C')),
    (b('mem_clear', 'MC'),  b('mem_read', 'MR'),  b('mem_save', 'MS'), b('mem_plus', 'M+'),      b('mem_minus', 'M-')),
    (b('sinus', 'sin'),     b('cosine', 'cos'),   b('tangent', 'tan'), b('logarithm_e', 'ln'),   b('root', '√')),
    (b('7', '7'),           b('8', '8'),          b('9', '9'),         b('division', '÷'),       b('degree_3', '^3')),
    (b('4', '4'),           b('5', '5'),          b('6', '6'),         b('multiplication', '×'), b('degree', '^')),
    (b('1', '1'),           b('2', '2'),          b('3', '3'),         b('minus', '-'),          b('change_sign', '±')),
    (b('0', '0'),           b('00', '00'),        b('dot', '·'),       b('plus', '+'),           b('equally', '=')),
)
