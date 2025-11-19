import psycopg2

def get_conexao():
    conn = psycopg2.connect(
        dbname = 'postgres',
        user = 'postgres.rhxtxwmqddjwquurwwkl',
        password = 'M@h03082006',
        host = 'aws-1-us-east-1.pooler.supabase.com',
        port = '6543'
    )
    return conn