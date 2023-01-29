from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from loguru import logger

from .settings import bot, dp, main_text, photo_style_text, photo_source_text, error_generate
from model.app import main


class Form(StatesGroup):
    image_style = State()
    image_source = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message) -> None:
    logger.info(f'User {message.from_user.id} {message.from_user.username} start')
    
    await message.answer(main_text)

@dp.message_handler(state='*', commands=['set_style'])
async def set_style_photo(message: types.Message):
    logger.info(f'Start {message.from_user.id} loading photo style')
    await Form.image_style.set()
    await message.reply(photo_style_text)


@dp.message_handler(state='*', commands=['set_source'])
async def set_source_photo(message: types.Message) -> None:
    logger.info(f'Start {message.from_user.id} loading photo source')
    await Form.image_source.set()
    await message.reply(photo_source_text)

# @dp.message_handler(state=Form.image_style, content_types=['photo'])
@dp.message_handler(state=[Form.image_source, Form.image_style], content_types=['photo'])
async def set_photo(message: types.Message, state: FSMContext):
    file_id = message.photo[-1].file_id
    logger.info(f'{message.from_user.id} loading {file_id}.jpg')
    # Form.image_style = file_id
    current_state = await state.get_state()
    dict_key = 'image_style' if current_state == 'Form:image_style' else 'image_source'
    
    async with state.proxy() as data:
        data[dict_key] = file_id
        if dict_key == 'image_source':
            data['size'] = [message.photo[-1].width, message.photo[-1].height]
    
    logger.info(data)

    await message.photo[-1].download(destination_file=f'app/uploaded_photos/{file_id}.jpg')

@dp.message_handler(state='*', commands=['generate'])
async def generate_photo(message: types.Message, state: FSMContext):
    logger.info(f'{message.from_user.id} generate photo')

    async with state.proxy() as data:
        if len(data) != 3:
            await message.answer(error_generate)
            return 

        logger.info('{} | source file: {} | image_file: {}'.format(message.from_user.id, data['image_source'], data['image_style']))
        output_file = main(data['image_source'], data['image_style'], data['size'],
                            epochs=20)

        with open(f'app/save_photos/{output_file}', 'rb') as photo_out:
            await bot.send_photo(chat_id=message.chat.id, photo=photo_out)

        
        
