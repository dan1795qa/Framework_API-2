from swagger_coverage_tool import SwaggerCoverageTracker
import httpx

# Инициализируем трекер для нашего сервиса "api-course"
# ВАЖНО: 'api-course' должен точно совпадать с ключом `key` в SWAGGER_COVERAGE_SERVICES
tracker = SwaggerCoverageTracker(service="api-course")