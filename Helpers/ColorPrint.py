import sys
class ColorPrint:
    '''
        @staticmethod
        def print_fail(message, end = '\n'):

        @staticmethod
        def print_pass(message, end = '\n'):
            
        @staticmethod
        def print_warn(message, end = '\n'):
            
        @staticmethod
        def print_info(message, end = '\n'):
            
        @staticmethod
        def print_bold(message, end = '\n'):           
    '''

    @staticmethod
    def print_fail(message, end = '\n'):
        sys.stderr.write('\x1b[1;31m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_pass(message, end = '\n'):
        sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_warn(message, end = '\n'):
        sys.stderr.write('\x1b[1;33m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_info(message, end = '\n'):
        sys.stdout.write('\x1b[1;34m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_bold(message, end = '\n'):
        sys.stdout.write('\x1b[1;37m' + message.strip() + '\x1b[0m' + end)
