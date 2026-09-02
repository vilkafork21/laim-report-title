import logging
import traceback
from typing import Dict, Any
from datetime import datetime as dt

from sdsautoval import *
from visualizer import TitleVisualizer

logger = logging.getLogger(__name__)


def main(
    development_report: Dict[str, Any],
    **kwargs) -> Dict[str, Any]:

    logger.info('Авторизация автовалидатора')
    autoval = AutoValidator()
    autoval.authorize_internal()
    
    logger.info(f'Получаем информацию из БМ по версии {kwargs.get('model_version_id', 'No model version specified')}')
    
    # try:
    #     mms_data = autoval._mms_service._client.get_model_version_info(kwargs.get('model_version_id'))
    # except exc:
    #     logger.info(f'Получена ошибка при получении информации о версии {kwargs.get('model_version_id')}')
    #     traceback.print_exc()
        
        
        
    logger.info('Формируем HTML-шапку отчёта о валидации.')
    html_report = TitleVisualizer().visualize(
        model_id=kwargs.get('model_id', ''),
        model_version_id=kwargs.get('model_version_id', ''),
        model_version_name=kwargs.get('model_version_name', ''),
        significance=kwargs.get('significance', ''),
        dev_block=kwargs.get('dev_block', ''),
        owner_block=kwargs.get('owner_block', ''),
        validator=kwargs.get('validator', ''),
        validation_date= dt.now().strftime('%d.%m.%Y'),
    )

    logger.info('HTML-шапка сформирована.')

    return {
        "hidden_port": html_report,
    }
