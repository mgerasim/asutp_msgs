

class ExtractNpsFromFileNameHelper:
    @staticmethod
    def run(file_name):
        if '01. НПС-23' in file_name:
            return 'NPS_23'
        if '02. НПС-24' in file_name:
            return 'NPS_24'
        if '03. НПС-26' in file_name:
            return 'NPS_26'
        if '04. НПС-27' in file_name:
            return 'NPS_27'
        if '05. НПС-29' in file_name:
            return 'NPS_29'
        if '06. НПС-30' in file_name:
            return 'NPS_30'
        if '07. НПС-32' in file_name:
            return 'NPS_32'
        if '08. НПС-34' in file_name:
            return 'NPS_34'
        if '09. НПС-36' in file_name:
            return 'NPS_36'
        if '10. НПС-38' in file_name:
            return 'NPS_38'
        if '11. НПС-40' in file_name:
            return 'NPS_40'
        if '12. НПС-41' in file_name:
            return 'NPS_41'
        if '13. НПС-1' in file_name:
            return 'NPS_1'
        if '14. НПС-2' in file_name:
            return 'NPS_2'
        if '15. НПС-3' in file_name:
            return 'NPS_3'

        raise
