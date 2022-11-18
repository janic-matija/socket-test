# Protokoli

## TCP

    Najcesce zastupljen

    Najsigurniji (potvrda uspesno poslatih paketa)

    Kasnjenje zbog cekanja na potvrde (u slucaju greske, salje se isti paket ponovo)

    Python: socket modul

    HSTCP
        High speed TCP  dobijen modifikacijom AIMD algoritma
                        Sirina prozora se povecava kada je veza 'sigurna'

## UDP

    Manje pouzdan (podaci se ne salju redom, nema ACK-a)

    Brzo slanje (nema cekanja na potvrde)    

    multicast, vise klijenata

    Python: socket modul

## UDT

    Baziran na UDP

    Koriscenje periodicnih potvrda (ACK) (potvrda nakon nekog vremena, ne za svaki paket)

    Python: odredjeni wrapper c++ biblioteke (nepotpun, verovatno kompatibilan sa python2)
