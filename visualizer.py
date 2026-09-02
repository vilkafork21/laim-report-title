from jinja2 import Template


class TitleVisualizer:
    """
    Visualizer for the validation report title page (шапка отчёта о монитоирнге).

    Generates an HTML fragment that reproduces the cover layout:
    - Top-left: model ID and model-version ID in italic
    - Centred heading: «Отчет о монитоирнге»
    - Centred sub-heading: model version name
    - Borderless two-column info table: significance degree, dev block,
      owner block, responsible validator, validation date
    """

    def __init__(self):
        self.html_template = Template("""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: #1a1a1a;
            overflow-wrap: break-word;
            word-break: break-word;
            hyphens: none;
        }

        .page {
            max-width: 960px;
            margin: 0 auto;
            padding: 32px 48px 48px 48px;
        }

        /* ── top-left IDs ── */
        .model-ids {
            font-style: italic;
            font-size: 0.95em;
            line-height: 1.5;
            color: #222;
            margin-bottom: 80px;
        }

        /* ── centred headings ── */
        .report-title {
            text-align: center;
            font-size: 2em;
            font-weight: bold;
            margin: 0 0 18px 0;
            color: #111;
        }

        .model-name {
            text-align: center;
            font-size: 1.55em;
            font-weight: normal;
            margin: 0 0 48px 0;
            color: #111;
        }

        /* ── info table ── */
        .info-table {
            width: 100%;
            margin: 0 auto;
            border-collapse: collapse;
            table-layout: fixed;
        }

        .info-table td {
            padding: 5px 8px;
            vertical-align: top;
            font-size: 1em;
            border: none;
            overflow-wrap: break-word;
            word-break: break-word;
            hyphens: none;     
        }

        .info-table td.label {
            width: 45%;
            color: #333;
        }

        .info-table td.value {
            color: #111;
        }

        .info-table tr.spacer td {
            padding-top: 18px;
        }
        
    </style>
</head>
<body>
<div class="page">

    <!-- top-left: model version ID (ID решения опционален — скрыт если пуст) -->
    <div class="model-ids">
        {% if model_id %}ID решения: {{ model_id }}<br>{% endif %}
        ID версии решения: {{ model_version_id }}
    </div>

    <!-- centred headings -->
    <div class="report-title">Отчет о результатах автомониторинга</div>
    {% if model_id %}<div style="text-align:center;font-size:1.2em;color:#444;margin:0 0 10px 0">GenAI-решение {{ model_id }}</div>{% endif %}
    <div class="model-name">{{ model_version_name }}</div>

    <!-- info table (no borders) -->
    <table class="info-table">
        <tbody>
            <tr>
                <td class="label">Степень значимости</td>
                <td class="value">{{ significance }}</td>
            </tr>
            <tr>
                <td class="label">Блок разработчика</td>
                <td class="value">{{ dev_block }}</td>
            </tr>
            <tr>
                <td class="label">Блок владельца</td>
                <td class="value">{{ owner_block }}</td>
            </tr>
            <tr class="spacer">
                <td class="label">Отчет подготовил</td>
                <td class="value">{{ validator }}</td>
            </tr>
            <tr>
                <td class="label">Дата подготовки</td>
                <td class="value">{{ validation_date }}</td>
            </tr>
        </tbody>
    </table>

</div>
</body>
</html>
        """)

    def visualize(
        self,
        model_id: str | int,
        model_version_id: str | int,
        model_version_name: str,
        significance: str,
        dev_block: str,
        owner_block: str,
        validation_date: str,
        validator: str,
    ) -> str:
        """
        Generate HTML for the validation report title page.

        Args:
            model_id:           Идентификатор модели (отображается слева сверху).
            model_version_id:   Идентификатор версии модели (отображается слева сверху).
            model_version_name: Название версии модели (под заголовком «Отчет о монитоирнге»).
            significance:       Степень значимости модели (например «С»).
            dev_block:          Блок разработчика.
            owner_block:        Блок владельца.
            validation_date:    Дата подготовки отчёта (например «02.12.2025»).
            validator:          ФИО ответственного валидатора.

        Returns:
            str: HTML-код шапки отчёта о монитоирнге.

        Example:
            >>> viz = TitleVisualizer()
            >>> html = viz.visualize(
            ...     model_id=292381,
            ...     model_version_id=292383,
            ...     model_version_name="Оффлайн модель против социальной инженерии",
            ...     significance="С",
            ...     dev_block='Блок «Сеть продаж»',
            ...     owner_block='Блок «Сеть продаж»',
            ...     validation_date="02.12.2025",
            ...     validator="Непомнящий Андрей Денисович",
            ... )
        """
        return self.html_template.render(
            model_id=model_id,
            model_version_id=model_version_id,
            model_version_name=model_version_name,
            significance=significance,
            dev_block=dev_block,
            owner_block=owner_block,
            validation_date=validation_date,
            validator=validator,
        )

    @staticmethod
    def save_to_file(html: str, filepath: str) -> None:
        """
        Save generated HTML to a file.

        Args:
            html:     HTML content to save.
            filepath: Destination file path.
        """
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

