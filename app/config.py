from pydantic import BaseSettings


class Settings(BaseSettings):
    url = 'https://glzqzgqavxxrhtgamenh.supabase.co'
    key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdsenF6Z3Fhdnh4cmh0Z2FtZW5oIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjcwMTQ1NjksImV4cCI6MTk4MjU5MDU2OX0.sG1sJqAxAweq7fnfJ_CcxFhXrDbjcgcm0WvMP14l43E'


settings = Settings()