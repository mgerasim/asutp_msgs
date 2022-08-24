class FieldFetcher:
    @staticmethod
    def DateCreatedFetch(columns, row):
        index = -1
        for column in columns:
            index += 1
            match column.value.upper():
                case 'ВРЕМЯ':
                    return row[index].value
                case 'ДАТА':
                    return row[index].value

    @staticmethod
    def MessageFetch(columns, row):
        index = -1
        for column in columns:
            index += 1
            match column.value.upper():
                case 'СООБЩЕНИЕ':
                    return row[index].value
                case 'ТЕКСТ СООБЩЕНИЯ':
                    return row[index].value

    @staticmethod
    def ObjectFetch(columns, row):
        index = -1
        for column in columns:
            index += 1
            match column.value.upper():
                case 'ОБЪЕКТ':
                    return row[index].value

        message = FieldFetcher.MessageFetch(columns=columns,
                                            row=row)

        message = message.strip('.')
        message = message.replace('_', '.')
        object = message.split('.')[0]
        return object

    @staticmethod
    def QualityFetch(columns, row) -> int:
        index = -1
        for column in columns:
            index += 1
            match column.value.upper():
                case 'КАЧЕСТВО':
                    return int(row[index].value)
                case 'ВАЖНСТЬ':
                    return int(row[index].value)

        return None

    @staticmethod
    def PriorityFetch(columns, row) -> str:
        index = -1
        for column in columns:
            index += 1
            match column.value.upper():
                case 'ПРИОРИТЕТ':
                    return row[index].value

    @staticmethod
    def ConvertQualityToSeverity(quality):
        match quality:
            # Нейтральные
            case 0:
                return 0
            case 1:
                return 0
            case 2:
                return 0
            case 50:
                return 0
            case 300:
                return 0
            # Предупредительные
            case 3:
                return 1
            case 100:
                return 1
            # Аварийные
            case 4:
                return 2
            case 200:
                return 2
            case _:
                raise Exception(f"""Неподдерживаемое качество #{quality}""")

    @staticmethod
    def ConvertPriorityToSeverity(priority: str) -> int:
        match priority.upper():
            # Нейтральный
            case 'НОРМАЛЬНЫЙ':
                return 0
            # Предупредительный
            case 'НИЗКИЙ':
                return 1
            case 'СРЕДНИЙ':
                return 1
            # Аварийный
            case 'ВЫСОКИЙ':
                return 2
            case _ :
                raise Exception(f"""Неподдерживаемый приоритет #{priority}""")

    @staticmethod
    def SeverityFetch(columns, row) -> int:
        quality = FieldFetcher.QualityFetch(columns, row)
        if quality is not None:
            severity = FieldFetcher.ConvertQualityToSeverity(quality)
            return severity
        else:
            priority = FieldFetcher.PriorityFetch(columns, row)
            if priority is None:
                match str(row[1].fill.start_color.rgb):
                    case 'FFFFFFFF':
                        return 0
                    case 'FF00FF00':
                        return 0
                    case 'FFFFFF00':
                        return 1
                    case 'FFFF0000':
                        return 2
                    case _:
                        raise Exception(f'Не удалось определить важность сообщения: {str(row[1].fill.start_color.rgb)}')
            severity = FieldFetcher.ConvertPriorityToSeverity(priority)
            return severity






