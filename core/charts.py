import json
import plotly.graph_objects as go


def build_bar_chart(title, x_values, y_values, y_axis_title, bar_color="#0f766e"):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=x_values,
            y=y_values,
            text=y_values,
            textposition="outside",
            marker_color=bar_color,
        )
    )

    fig.update_layout(
        title=title,
        template="plotly_white",
        xaxis_title="Categoría",
        yaxis_title=y_axis_title,
        showlegend=False,
        margin=dict(t=50, r=20, b=60, l=50),
    )

    fig.update_traces(cliponaxis=False)

    return json.loads(fig.to_json())


def build_grouped_bar_chart(title, x_values, series):
    fig = go.Figure()

    for item in series:
        fig.add_trace(
            go.Bar(
                name=item["name"],
                x=x_values,
                y=item["values"],
            )
        )

    fig.update_layout(
        title=title,
        template="plotly_white",
        barmode="group",
        xaxis_title="Partidos",
        yaxis_title="Valor",
        margin=dict(t=50, r=20, b=60, l=50),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
        ),
    )

    fig.update_traces(cliponaxis=False)

    return json.loads(fig.to_json())


def build_line_chart(title, x_values, y_values, y_axis_title, line_color="#2563eb"):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x_values,
            y=y_values,
            mode="lines+markers",
            fill="tozeroy",
            line=dict(color=line_color, width=3),
            marker=dict(size=8),
            name=y_axis_title,
        )
    )

    fig.update_layout(
        title=title,
        template="plotly_white",
        xaxis_title="Partidos",
        yaxis_title=y_axis_title,
        showlegend=False,
        margin=dict(t=50, r=20, b=60, l=50),
    )

    return json.loads(fig.to_json())


def build_donut_chart(title, labels, values):
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.5,
                textinfo="label+percent",
            )
        ]
    )

    fig.update_layout(
        title=title,
        template="plotly_white",
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02,
        ),
        uniformtext_minsize=12,
        uniformtext_mode="hide",
        margin=dict(t=50, r=20, b=20, l=20),
    )

    return json.loads(fig.to_json())