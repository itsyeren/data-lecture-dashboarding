# Dash examples

`singlepage` folder’ında, basitten karmaşığa doğru tek sayfalık app’ler:

- `minimal.py`
- `twocols.py`
- `app.py`: dropdown içeren çalışan bir app
- `withamap.py`: map ekleyen örnek

`multipage` folder’ında, mevcut page’leri temel bir multipage app içinde birleştiren örnek var.

`nextlevel` folder’ında ise, aynı app’in bootstrap ve layout kullanılarak geliştirilmiş hali var. Bu, sizden beklediğimiz seviyenin oldukça ötesine geçiyor, ancak web geçmişiniz varsa bununla oynayabilirsiniz.

## Setup

`emissions.csv` file’ını indirmeniz gerekecek:

1. Çalıştırmak istediğiniz page’in bulunduğu folder’a gidin.
2. Terminal’de aşağıdaki command’i çalıştırın:

    ```bash
    curl -s https://raw.githubusercontent.com/owid/co2-data/refs/heads/master/owid-co2-data.csv > emissions.csv
    ```

Başka bir page’i çalıştırmak isterseniz, `emissions.csv` file’ını ilgili folder’a kopyalayın veya taşıyın.
