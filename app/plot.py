import json
import plotly.graph_objects as go
import numpy as np

def plotly_decision_boundary(X, y, new_pt, pred_label, clf, mesh_size = 0.05, margin = 0.25):

  labels = ["Cat", "Dog"]
  colors = ["blue", "red"]

  x_min, x_max = X[:, 0].min() - margin, X[:, 0].max() + margin
  y_min, y_max = X[:, 1].min() - margin, X[:, 1].max() + margin
  x_range = np.arange(x_min, x_max, mesh_size)
  y_range = np.arange(y_min, y_max, mesh_size)
  xx, yy = np.meshgrid(x_range, y_range)
  grid = np.c_[xx.ravel(), yy.ravel()]
  Z = clf.predict(grid).reshape(xx.shape)

  # Build plot
  fig = go.Figure()

  # Decision boundary
  fig.add_trace(go.Contour(
      x=x_range,
      y=y_range,
      z=Z,
      showscale=False,
      colorscale=[[0, 'rgba(135,206,250,1)'], [1, 'rgba(255,182,193,1)']],
      opacity=0.3,
      contours=dict(showlines=False),
      hoverinfo='skip'
  ))

  for class_val in np.unique(y):
      mask = y == class_val
      fig.add_trace(go.Scatter(
          x=X[mask, 0],
          y=X[mask, 1],
          mode='markers',
            marker=dict(
                size=6,
                color=colors[class_val],
                line=dict(width=1, color="black")  # edge line
            ),
            name=labels[class_val]
      ))

  fig.add_trace(go.Scatter(
    x=[new_pt[0]],
    y=[new_pt[1]],
    mode='markers',
    marker=dict(
        size=16,
        color='yellow',
        symbol='star',
        line=dict(width=1.5, color='black')
    ),
    name="Your Image ("+labels[pred_label]+")"
  ))

  fig.update_layout(
    paper_bgcolor="#eee",
    plot_bgcolor="#eee",
    margin=dict(l=0, r=0, t=0, b=0),  # removes whitespace around plot
    font=dict(family="system-ui", size=14, color="black"),
    xaxis=dict(
        range=[x_min, x_max],
        showgrid=True,
        gridcolor="black",
        gridwidth=1,
        showticklabels=False,
        ticks='',
        showline=False,
        zeroline=False
    ),
    yaxis=dict(
        range=[y_min, y_max],
        showgrid=True,
        gridcolor="black",
        gridwidth=1,
        showticklabels=False,
        ticks='',
        showline=False,
        zeroline=False
    ),
      legend=dict(
        x=0,       # left edge
        y=1,       # top edge
        xanchor='left',
        yanchor='top',
        bgcolor='rgb(255,255,255)',
        bordercolor='black',
        borderwidth=1
    )
  )

  return fig.to_json()