from gym.envs.registration import register

import gym
from test_env.envs import *

register(
    id='Fourrooms-v1',
    entry_point='test_env.envs.fourrooms:Fourrooms',
    kwargs={
        'map_name': '9x9',
    })

register(
    id='Fourroomssto-v1',
    entry_point='test_env.envs.fourroom_sto:Fourroomssto',
)

register(
    id='KeyDoor-v1',
    entry_point='test_env.envs.key_door:KeyDoor',
)

register(
    id='DoubleCartPole-v1',
    entry_point='test_env.envs.double_cart_pole:MultipleCartPoleEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)

register(
    id='QuadCartPole-v1',
    kwargs={
        'num_tasks': 4,
    },
    entry_point='test_env.envs.double_cart_pole:MultipleCartPoleEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)

register(
    id='16CartPole-v1',
    kwargs={
        'num_tasks': 16,
    },
    entry_point='test_env.envs.double_cart_pole:MultipleCartPoleEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)
