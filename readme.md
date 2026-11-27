# Registrering og innlogging

Jeg har lagt til to nye sider på kantinenettsiden: en side for å lage bruker og en side for å logge inn. Brukerne lagres i en MySQL-database.

## Registrer (`/register`)

1. Brukeren skriver inn navn, brukernavn og passord og trykker «Registrer».
2. Flask henter det som ble skrevet med `request.form`.
3. Jeg kobler til databasen og kjører en `INSERT`, som legger brukeren inn i tabellen `kunder`.
4. `conn.commit()` lagrer endringen. Uten den blir ikke brukeren lagret.
5. Brukeren sendes videre til innloggingssiden.

## Logg inn (`/login`)

1. Brukeren skriver inn brukernavn og passord og trykker «Logg inn».
2. Flask henter det som ble skrevet med `request.form`.
3. Jeg kobler til databasen og kjører en `SELECT`, som leter etter en bruker med det brukernavnet og passordet.
4. `fetchone()` henter svaret. Her trengs ingen `commit()`, fordi `SELECT` bare leser og ikke endrer noe.
5. Hvis brukeren finnes, vises en velkomstside med navnet. Hvis ikke, står det «Feil brukernavn eller passord».

## Databasen

Databasen heter `login`, og tabellen heter `kunder`:

```sql
CREATE TABLE kunder (
  kunde_id   INT NOT NULL AUTO_INCREMENT,
  navn       VARCHAR(255),
  brukernavn VARCHAR(255) UNIQUE,
  passord    VARCHAR(255),
  PRIMARY KEY (kunde_id)
);
```

## Filer jeg har endret

- `app.py`: koden for `/register` og `/login`, og `get_conn()`, som kobler til databasen
- `templates/register.html`: skjemaet for å registrere seg
- `templates/login.html`: skjemaet for å logge inn
- `templates/welcome.html`: siden du ser når du har logget inn
- `templates/base.html`: lenker til de nye sidene i menyen


