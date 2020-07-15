from cloud_info_provider.publishers.base import BasePublisher

class CMDBPublisher(BasePublisher):
    @staticmethod
    def populate_parser(parser):
        parser.add_argument(
            '--cmdb-read-endpoint',
            metavar='URL',
            help='Specify CMDB read URL')
        parser.add_argument(
            '--cmdb-write-endpoint',
            metavar='URL',
            help='Specify CMDB write URL')
        parser.add_argument(
            '--cmdb-db-user',
            metavar='USERNAME',
            help=('With password authentication, this specifies CMDB username'))
        parser.add_argument(
            '--cmdb-db-pass',
            metavar='PASSWORD',
            help=('With password authentication, this specifies CMDB password'))
        parser.add_argument(
            '--cmdb-data-file',
            metavar='JSON_FILE',
            help=('Specify a JSON file for CMDB data rather than '
                  'getting remotely'))
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Do not post to remote CMDB service')
