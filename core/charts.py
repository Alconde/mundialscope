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
        xaxis_title="Selección",
        yaxis_title=y_axis_title,
        showlegend=False,
        margin=dict(t=50, r=20, b=60, l=50),
    )

    fig.update_traces(cliponaxis=False)

    return json.loads(fig.to_json())