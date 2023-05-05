import os
from alembic.config import CommandLine, Config
from marketparser.utils.pg import DEFAULT_PG_URL
from pathlib import Path

PROJECT_PATH = Path(__file__).parent.parent.resolve()

def main():
    alembic = CommandLine()
    alembic.parser.add_argument(
        '--pg-url', default=os.getenv('MARKETPARSER_PG_URL', DEFAULT_PG_URL),
        help='Database URL [env var: MARKETPARSER_PG_URL]'
    )
    options = alembic.parser.parse_args()

    if not os.path.isabs(options.config):
        options.config = os.path.join(PROJECT_PATH, options.config)

    config = Config(file_=options.config, ini_section=options.name, cmd_opts=options)

    config.set_main_option('sqlalchemy.url', options.pg_url)

    exit(alembic.run_cmd(config, options))

if __name__ == '__main__':
    main()
