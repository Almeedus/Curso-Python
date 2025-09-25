from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error('Passou no erro')
lp.log_success('Passou no sucesso')

lf = LogFileMixin()
lf.log_error('Error no arquivo')
lf.log_success('Sucesso no arquivo')