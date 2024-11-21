import pytest
from television import Television


def test_init():
    tv = Television()
    expected_output = f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'
    assert str(tv) == expected_output, 'Initial TV state Error'


def test_power():
    tv = Television()
    tv.power()
    assert tv.status, 'TV should turn on after power is toggled'
    tv.power()
    assert not tv.status, 'TV should turn off after power is toggled'


def test_mute():
    tv = Television()
    tv.mute()
    assert not tv.muted, 'TV should not mute when off'

    tv.power()
    tv.mute()
    assert tv.muted, 'TV should mute when turned on'
    tv.mute()
    assert not tv.muted, 'TV should un-mute when toggled again'


def test_channel_up():
    tv = Television()
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL, 'Channel should not change when TV is off'

    tv.power()
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL + 1, 'Channel should increase by 1'

    tv.channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL, 'Channel should wrap around to min'


def test_channel_down():
    tv = Television()
    tv.channel_down()
    assert tv.channel == Television.MIN_CHANNEL, 'Channel should not change when TV is off'

    tv.power()
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL, 'Channel should wrap around to max'

    tv.channel = Television.MAX_CHANNEL
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL - 1, 'Channel should decrease by 1'


def test_volume_up():
    tv = Television()
    tv.volume_up()
    assert tv.volume == Television.MIN_VOLUME, 'Volume should not change when TV is off'

    tv.power()
    tv.volume_up()
    assert tv.volume == Television.MIN_VOLUME + 1, 'Volume should increase by 1'

    tv.volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv.volume == Television.MAX_VOLUME, 'Volume should not go past maximum'

    tv.muted = True
    tv.volume_up()
    assert not tv.muted, 'Volume up should un-mute the TV'


def test_volume_down():
    tv = Television()
    tv.volume_down()
    assert tv.volume == Television.MIN_VOLUME, 'Volume should not change when TV is off'

    tv.power()
    tv.volume = Television.MAX_VOLUME
    tv.volume_down()
    assert tv.volume == Television.MAX_VOLUME - 1, 'Volume should decrease by 1'

    tv.volume = Television.MIN_VOLUME
    tv.volume_down()
    assert tv.volume == Television.MIN_VOLUME, 'Volume should not go below min'

    tv.muted = True
    tv.volume_down()
    assert not tv.muted, 'Volume down should un-mute TV'