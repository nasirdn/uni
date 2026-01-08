import multiprocessing
import logging
from typing import List, Dict
from services.conversion_service import ConversionService

logger = logging.getLogger(__name__)


class RequestProcessor:
    def __init__(self, max_workers=None):
        self.max_workers = max_workers or multiprocessing.cpu_count()
        self.conversion_service = ConversionService()

    def _convert_single(self, conversion_data: Dict) -> Dict:
        """Обработка одной конвертации (используется в процессах)"""
        try:
            result = self.conversion_service.convert(
                conversion_data['amount'],
                conversion_data['from'],
                conversion_data['to']
            )
            return {
                'success': True,
                'input': conversion_data,
                'result': result
            }
        except Exception as e:
            return {
                'success': False,
                'input': conversion_data,
                'error': str(e)
            }

    def process_batch_conversions(self, conversions: List[Dict]) -> List[Dict]:
        """
        Многопроцессная обработка пакета конвертаций
        """
        if not conversions:
            return []

        # Ограничиваем количество воркеров
        num_workers = min(self.max_workers, len(conversions), multiprocessing.cpu_count())

        logger.info(f"Processing {len(conversions)} conversions using {num_workers} workers")

        try:
            # Создаем пул процессов
            with multiprocessing.Pool(processes=num_workers) as pool:
                # Маппим задачи на процессы
                results = pool.map(self._convert_single, conversions)

            logger.info(f"Batch processing completed: {len(results)} results")
            return results

        except Exception as e:
            logger.error(f"Batch processing error: {e}")

            # Fallback: последовательная обработка
            logger.info("Falling back to sequential processing")
            results = []
            for conv in conversions:
                try:
                    result = self.conversion_service.convert(
                        conv['amount'],
                        conv['from'],
                        conv['to']
                    )
                    results.append({
                        'success': True,
                        'input': conv,
                        'result': result
                    })
                except Exception as inner_e:
                    results.append({
                        'success': False,
                        'input': conv,
                        'error': str(inner_e)
                    })

            return results