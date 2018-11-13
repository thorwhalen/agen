import numpy as np

DFLT_SR = 44100
DFLT_CHK_SIZE_FRM = 21 * 2048
DFLT_MAX_AMPLITUDE = 30000
DFLT_PATTERN_LEN = 100
DFLT_PATTERN = [DFLT_MAX_AMPLITUDE] * 10 + [-DFLT_MAX_AMPLITUDE] * 10


def chk_from_pattern(chk_size_frm=DFLT_CHK_SIZE_FRM, pattern=None):
    if pattern is None:
        pattern = np.random.randint(-DFLT_MAX_AMPLITUDE, DFLT_MAX_AMPLITUDE, DFLT_PATTERN_LEN)
    return np.tile(pattern, reps=int(np.ceil(chk_size_frm / float(len(pattern)))))[:chk_size_frm].astype(np.int16)


def random(chk_size_frm=DFLT_CHK_SIZE_FRM, max_amplitude=DFLT_MAX_AMPLITUDE):
    return np.random.randint(-max_amplitude, max_amplitude, chk_size_frm).astype(np.int16)


def pure_tone(chk_size_frm=DFLT_CHK_SIZE_FRM, freq=440, sr=DFLT_SR, max_amplitude=DFLT_MAX_AMPLITUDE):
    pattern_length = int(sr / freq)
    pattern = max_amplitude * np.sin(np.linspace(0, 2 * np.pi, pattern_length))
    return chk_from_pattern(chk_size_frm, pattern)


def triangular_tone(chk_size_frm=DFLT_CHK_SIZE_FRM, freq=440, sr=DFLT_SR, max_amplitude=DFLT_MAX_AMPLITUDE):
    pattern_length = int(sr / freq)
    pattern = np.arange(-max_amplitude, max_amplitude, pattern_length)
    return chk_from_pattern(chk_size_frm, pattern)


def square_tone(chk_size_frm=DFLT_CHK_SIZE_FRM, freq=440, sr=DFLT_SR, max_amplitude=DFLT_MAX_AMPLITUDE):
    pattern_length = int(sr / freq)
    half_pattern_length = int(pattern_length / 2)  # oh well for the plus minus 1
    pattern = [max_amplitude] * half_pattern_length + [-max_amplitude] * half_pattern_length
    return chk_from_pattern(chk_size_frm, pattern)